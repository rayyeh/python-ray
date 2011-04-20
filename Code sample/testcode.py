#######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#'*60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#'*60

import sys
from socket import *

serverHost = '192.168.110.79'
serverPort = 6001

message = '0062Q100039500012   4514453690007903FFFF1249                      '

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

#Create a socket
sSock = socket(AF_INET, SOCK_STREAM)

#Connect to server
sSock.connect((serverHost, serverPort))

#Send messages
for i in range(1,1000):
    sSock.send(message)
    data = sSock.recv(1024)
    print 'Client received:',data

sSock.close()
    

    