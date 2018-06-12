#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '127.0.0.1'
port = 9999

ServerSocket.bind((address,port))

ServerSocket.listen(5)
print('服务器已启动')

while True:
    ClientConn, ClinetAddress = ServerSocket.accept()
    print('客户端连接地址：%s' % str(ClinetAddress))
    data = ClientConn.recv(1024):
    print('客户端发来信息：%s' % data.decode('utf-8'))
    ClientConn.send(b'hello client!')
    ClientConn.close()



