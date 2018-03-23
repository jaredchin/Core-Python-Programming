from socket import *
import sys
from threading import *

if len(sys.argv) < 3:
    HOST = 'localhost'
    PORT = 51423
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

BUFSIZ = 1024
ADDR = (HOST, PORT)


def handlesend(tcpCliSock):
    while True:
        sdata = input('> ')
        if not sdata:
            break
        tcpCliSock.send(sdata.encode())

    tcpCliSock.close()


tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 建立发送消息的线程
s = Thread(target=handlesend, args=[tcpCliSock])
s.setDaemon(1)
s.start()

while True:
    rdata = tcpCliSock.recv(BUFSIZ)
    if not rdata:
        break
    print(rdata)

tcpCliSock.close()
