# -*- coding:utf-8 -*-

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 9999))

print(s.recv(1024))

for data in ['zhang', 'liu', 'wang']:
    s.send(data.encode())
    print(s.recv(1024))

s.send("exit".encode())
print(s.recv(1024))

print("ok connection will exit for 10 Seconds")
time.sleep(10)
s.close()
