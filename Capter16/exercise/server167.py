from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connect from:', addr)

    while True:
        rdata = tcpCliSock.recv(BUFSIZ)
        if not rdata:
            break
        print(rdata)
        sdata = input('>')
        tcpCliSock.send(('[%s] %s' % (ctime(), sdata)).encode())
    tcpCliSock.close()
tcpSerSock.close()