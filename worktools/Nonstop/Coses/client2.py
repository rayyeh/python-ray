#######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#'*60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#'*60

import sys,time
from socket import *

serverHost = '192.168.110.93'
serverPort = 12343

message = 'Hello'

def now():
	return time.ctime(time.time( ))

message = 'Hello:'+now()

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

#Create a socket
sSock = socket(AF_INET, SOCK_STREAM)

#Connect to server
sSock.connect((serverHost, serverPort))

#Send messages
sSock.send(message)
data = sSock.recv(1024)
print 'Client received: ', data

sSock.close()
    

