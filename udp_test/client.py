import socket

host = '127.0.0.1'  # 这个是客户端的ip地址
port = 1234  # 端口选择大于10000的,避免和系统的冲突
bufsize = 1024  # 定义缓冲大小

addr = (host, port)
udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建客户端

while True:
    data = input('>>> ')
    if not data:
        break
    data = data.encode(encoding = 'utf-8')
    udpClient.sendto(data, addr)  # 发送数据
    data, addr = udpClient.recvfrom(bufsize)  # 接收数据和返回地址
    print(data.decode(encoding = 'utf-8'), 'from', addr)

udpClient.close()