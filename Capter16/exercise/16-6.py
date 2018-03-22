from socket import *


PORT = getservbyname('daytime', 'udp')
HOST = 'localhost'
BUFSIZ = 1024

ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)
data = input('>')

udpCliSock.sendto(data.encode(), ADDR)
data, ADDR = udpCliSock.recvfrom(BUFSIZ)

print(data)
udpCliSock.close()