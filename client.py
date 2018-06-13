#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import socket
import threading
#import User

def main():
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('客户端套接字已创建......')
    address = '127.0.0.1'
    port = 9999
    print('连接对象地址及端口已设置......')
    ClientSocket.connect((address,port))
    print('服务器已连接......')

    #thr = threading.Thread(XXX, (user,))
    #thr.start()

    while True:
        msg = input('请输入聊天内容：')
        if str(msg) == 'exit':
            break
        ClientSocket.send(msg.encode('utf-8'))
        data = ClientSocket.recv(1024)
        print('接收服务器信息为：', data.decode('utf-8'))

    ClientSocket.close()

    
if __name__ == '__main__':
    main()
