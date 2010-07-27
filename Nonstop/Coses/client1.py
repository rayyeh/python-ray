#######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#'*60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#'*60

import sys
from socket import *

serverHost = '192.168.113.2'
serverPort = 5008

message = ['Client Message1 come ', 'Client Message2 come']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

#Create a socket
sSock = socket(AF_INET, SOCK_STREAM)

#Connect to server
sSock.connect((serverHost, serverPort))

#Send messages
for item in message:
    sSock.send(item)
    data = sSock.recv(1024)
    print 'Client received: ', data

sSock.close()
    

