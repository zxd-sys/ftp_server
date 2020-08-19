"""
author: zxd
email: 2115296503@qq.com
time: 2020-8-17
env: python3
Thread and socket
"""
from socket import *
from threading import Thread
from signal import *
import os, time

HOST = "0.0.0.0"
PORT = 22225
ADDR = (HOST, PORT)
DIR = "day04/"


# 创建自己的线程类
class MyThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    # 重写run()
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == "EXIT":
                break
            elif data == "LIST":
                self.get_listdir()
            elif data[:3] == "PUT":
                self.up_dir(data.split(" ")[-1])
            elif data[:3] == "GET":
                self.down_dir(data.split(" ")[-1])

    # 创建获取文件库所有文件名的函数
    def get_listdir(self):
        msg = os.listdir(DIR)
        if not msg:
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            # 防止粘连
            time.sleep(0.1)
            file = "\n".join(msg)
            # 发送文件名
            self.connfd.send(file.encode())

    # 创建上传文件的函数
    def up_dir(self, filename):
        if os.path.exists(DIR + filename):
            self.connfd.send(b"FALE")
            return
        self.connfd.send(b"OK")
        # 接收文件
        fw = open(DIR + filename, "wb")
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            else:
                fw.write(data)
        fw.close()

    # 创建下载文件的函数
    def down_dir(self, filename):
        # 判断文件是否存在,再分项处理
        try:
            f = open(DIR + filename,"rb")
        except:
            self.connfd.send(b"FAIL")
            return
        self.connfd.send(b"OK")
        time.sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                break
            self.connfd.send(data)
        f.close()
        time.sleep(0.1)
        self.connfd.send(b"##")




def main():
    # 创建套接字
    sock = socket()
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(ADDR)
    sock.listen(5)
    # 处理僵尸进程
    signal(SIGCHLD, SIG_IGN)
    while True:
        try:
            connfd, addr = sock.accept()
            print("connect from ", addr)
        except KeyboardInterrupt:
            sock.close()
            return
        t = MyThread(connfd)
        t.start()


if __name__ == '__main__':
    main()
