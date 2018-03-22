from socket import *


BUFSIZ = 1024
HOST = input('host:')
PORT = input('port:')
if not HOST:
    HOST = 'localhost'
if not PORT:
    PORT = 21567
PORT = int(PORT)
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

tcpCliSock.close()
