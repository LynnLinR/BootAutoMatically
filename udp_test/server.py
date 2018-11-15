import socket
import time

host = ''  # 监听所有发送过来的ip
port = 1234  # 开放接口
bufsize = 1024  # 内存大小
addr = (host, port)

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(addr)  # 开始监听

while True:
    print('Waiting for connection...')
    data, addr = udpServer.recvfrom(bufsize)  # 接收数据和返回地址
    data = data.decode(encoding='utf-8')  # 最好进行解码的同时指定编码格式,以免编码不同导致的bug
    data = "at %s :%s" % (time.ctime(), data)
    udpServer.sendto(data.encode(encoding='utf-8'), addr)

    print('... recevied from and return to:', addr)
    print("data it's:", data)

udpServer.close()
