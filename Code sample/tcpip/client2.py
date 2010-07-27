#######################################################
## Demo:Sending Streaming Data
#######################################################
print '#'*60
print '# Demo:Sending Streaming Data'
print '#'*60

import sys
from socket import *

serverHost = '127.0.0.1'
serverPort = 50007

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

#Create socket
sSock = socket(AF_INET, SOCK_STREAM)

#Connect to server
sSock.connect((serverHost, serverPort))

#Stream data to server.
line = ""
while line != 'bye':
    line = raw_input("Send to %s: " % (serverHost))
    sSock.send(line+'\n')
    data = sSock.recv(1024)
    print data

sSock.shutdown(0)
sSock.close()
