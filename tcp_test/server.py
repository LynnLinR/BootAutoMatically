import socket
import threading
import time


def tcplink(sock, addr):
    print("Accept new connection from %s:%s ..." % addr)
    print(sock)
    sock.send('Welcome!'.encode())

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == "exit".encode or not data:
            sock.send("client exit!".encode())
            break
        else:
            sock.send("Hello,%s!".encode() % data)
    sock.close()
    print("Connection from %s:%s closed." % addr)


def main():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听端口
    s.bind(("127.0.0.1", 9999))

    s.listen(5)
    print("Waiting for connecetion...")

    while True:
        # 接受一个新连接
        sock, addr = s.accept()

        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink(sock, addr))
        t.start()


if __name__ == "__main__":
    main()
