#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

ClietnSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '127.0.0.1'
port = 9999

ClietnSocket.connect((address,port))
print('客户端已启动')

ClietnSocket.send(b'hello world!')

data = ClietnSocket.recv(1024)
print(data.decode('utf-8'))

ClietnSocket.close()
