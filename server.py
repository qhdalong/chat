#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import socket
import threading
import User

#全局变量，用户表
userlist = []
userlist_length = 0

def hand_user_conn(user):
    global userlist,userlist_length

    while True:
        data = user.conn.recv(1024)
        if len(data)>0:
            if data.decode('utf-8')=='exit':
                user.logout()
                userlist.remove(user)
                userlist_length -= 1
                break
            print('用户[%s]说：%s' % (str(user.name),str(data.decode('utf-8'))))
            msg = '服务器已收到'
            user.conn.send(msg.encode('utf-8'))


def main():
    global userlist,userlist_length

    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('服务器套接字已创建......')
    address = '127.0.0.1'
    port = 9999
    print('服务器地址及端口已设置......')
    ServerSocket.bind((address,port))
    print('服务器地址及端口已绑定......')
    ServerSocket.listen(5)
    print('服务器监听进程已开启......')
    print('服务器已启动......')
    while True:
        ClientConn, ClinetAddress = ServerSocket.accept()
        user = User.User(ClientConn, userlist_length, ClinetAddress)      
        print('用户[%s]已连接' % str(userlist_length))
        userlist.append(user)
        userlist_length += 1
        thr = threading.Thread(target=hand_user_conn, args=(user,))
        thr.start()
  

if __name__ == '__main__':
    main()



