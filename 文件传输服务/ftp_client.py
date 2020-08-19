"""
ftp_client
"""
from socket import *
import time
import sys

sock = socket()
HOST = "127.0.0.1"
PORT = 22225
ADDR = (HOST, PORT)


# 创建客户端类
class FtpClient:
    def __init__(self, sock):
        self.sock = sock

    # 创建获取目标文件库文件名的函数
    def get_listdir(self):
        # 发送请求
        self.sock.send(b"LIST")
        # 等待反馈,分类处理
        data = self.sock.recv(128)
        if data == b"OK":
            files = self.sock.recv(1024 * 1024)
            print("文件库文件为:\n", files.decode())
        else:
            print("文件库为空!")

    # 创建上传文件的函数
    def up_dir(self, filename):
        try:
            f = open(filename, "rb")
        except:
            print("该文件不存在!")
            returngit
        # 提取真正的文件名
        filename = filename.split("/")[-1]
        msg = "PUT " + filename
        self.sock.send(msg.encode())
        # 等待回复,更具回复判断如何处理
        result = self.sock.recv(128)
        if result == b"OK":
            # 上传文件
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.sock.send(data)
            f.close()
            time.sleep(0.1)
            self.sock.send(b"##")
        else:
            print("该文件已在文件库中存在!")

    # 创建下载文件的的函数
    def down_dir(self, filename):
        data = "GET " + filename
        self.sock.send(data.encode())
        # 等待反馈,分类处理
        msg = self.sock.recv(128)
        if msg == b"OK":
            fw = open("day04副本/" + filename, "wb")
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                else:
                    fw.write(data)
            fw.close()
        else:
            print("文件不存在!")

    # 创建退出函数
    def exit01(self):
        self.sock.send(b"EXIT")
        self.sock.close()
        sys.exit("谢谢使用!")


# 创建客户端主函数
def main():
    sock = socket()
    sock.connect(ADDR)
    ftpClient = FtpClient(sock)
    while True:
        print("""
        ==============文件传输功能列表================
                 LIST-> 查看文件库中所有文件名
                 PUT -> 上传文件到文件库
                 GET -> 下载文件到指定文件夹
                 EXIT-> 退出
        ============================================
        """)
        tmp = input("请输入指令:")
        if tmp == "LIST":
            ftpClient.get_listdir()

        elif tmp[:3] == "PUT":
            ftpClient.up_dir(tmp.split(" ")[-1])
        elif tmp[:3] == "GET":
            ftpClient.down_dir(tmp.split(" ")[-1])
        elif tmp == "EXIT":
            ftpClient.exit01()


if __name__ == '__main__':
    main()
