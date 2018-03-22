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

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)
udpCliSock.close()