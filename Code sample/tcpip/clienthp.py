from builtins import str
from builtins import range
# ######################################################
# # Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#' * 60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#' * 60

import sys
from socket import *

serverHost = '192.168.110.93'
serverPort = 15000

message = ['Client Message1 come ', 'Client Message2 come']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

#Create a socket
sSock = socket(AF_INET, SOCK_STREAM)

#Connect to server
sSock.connect((serverHost, serverPort))

#Send messages
#for item in message:
for i in range(1, 20000):
    item = 'send from nonstop:' + str(i)
    sSock.send(item)
    data = sSock.recv(1024)
    print 'Client received: ', data

sSock.close()
    

