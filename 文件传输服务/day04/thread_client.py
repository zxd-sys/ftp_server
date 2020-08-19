"""
 tcp客户端循环示例
"""
from socket import *

addr = ('127.0.0.1', 22228)
# 创建tcp套接字

tcp_socket = socket(AF_INET, SOCK_STREAM)
# 发起链接
tcp_socket.connect(addr)
while True:

    # 发消息
    msg = input(">>>")
    # 循环退出方案二,不通知服务端
    if not msg:
        break
    tcp_socket.send(msg.encode())
    # 循环退出方案一
    # if msg == "quit":
    #     break
    # 接收消息
    data = tcp_socket.recv(1024)
    print("接收到服务端消息:", data.decode())

# 关闭
tcp_socket.close()