#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

ClietnSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '127.0.0.1'
port = 9999

ClietnSocket.connect((address,port))
print('客户端已启动')

choice = 1

while choice:
    msg = input('请输入聊天内容：')
    choice = input('choice:')

    ClietnSocket.send(msg.encode('utf-8'))

    data = ClietnSocket.recv(1024)
    print('接收服务器信息为：', data.decode('utf-8'))

ClietnSocket.close()
