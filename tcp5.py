
# coding=utf-8
# !/usr/bin/env python
 
 
from socket import *
from time import ctime
import threading
import time
 
HOST = ''
PORT = 8001
BUFSIZ = 1024
ADDR = (HOST, PORT)
 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
socks = []  # 放每个客户端的socket
 
 
def handle():
    while True:
        for s in socks:
            try:
                request_data = s.recv(1024)
                print("-"*40)
                print(socks)
                print()
                print()
                print(s)
                print('request data:', request_data)
        
            except Exception as e:
                continue

            if not request_data:
                socks.remove(s)
                s.close()
                continue

            # 构造响应数据
            response_data = '傻逼再见'

            # 发送响应数据
            s.send(bytes(response_data,'utf-8'))
 
 
t = threading.Thread(target=handle)  # 子线程
if __name__ == '__main__':
    t.start()
    print('waiting for connecting...')
    while True:
        clientSock, addr = tcpSerSock.accept()
        print('connected from:', addr)
        clientSock.setblocking(0)
        socks.append(clientSock)
        print(socks)
 
