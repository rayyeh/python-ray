#######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#'*60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#'*60

import sys
from socket import *
import binascii

serverHost = '192.168.110.91'
serverPort = 1658

message1 ='0058'
message2="ISO00600006008008220000000010000040000000000000011130911150133610176011101122M009012001"
message3=binascii.a2b_hex(message1)+message2
print message3

#Create a socket
sSock = socket(AF_INET, SOCK_STREAM)

#Connect to server
sSock.connect((serverHost, serverPort))
print 'connecting:',serverHost
#Send messages
sSock.send(message3)
data = sSock.recv(100)
print 'Client received: ', data

#sSock.close()
    

