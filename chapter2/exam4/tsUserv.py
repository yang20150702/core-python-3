# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 09:16:08 2016

@author: yang
"""

from socket import *
from time import ctime

HOST = ''
PORT = 23456
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print('waiting for message..')
        data, addr = udpSerSock.recvfrom(BUFSIZE)
        udpSerSock.sendto('[%s] %s'.encode('utf-8')% (bytes(ctime(), 'utf-8'), data), addr)
        
        print('...received from and returned to:', addr)
finally:
    udpSerSock.close()
    