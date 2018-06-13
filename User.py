#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

class User:
    def __init__(self, conn, name, address):
        self.conn = conn
        self.name = name
        self.address = address

    def send_msg(self, msg):
        self.conn.send(msg)

    def logout(self):
        self.conn.close()