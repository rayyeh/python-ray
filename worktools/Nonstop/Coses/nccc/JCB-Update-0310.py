from builtins import hex
# ######################################################
## Demo:Opening a Server-Side Socket for Receiving Data
#######################################################
print '#' * 60
print '# Demo:Opening a Server-Side Socket for Receiving Data'
print '#' * 60

from socket import *
import binascii

serverHost = ''  # listen on all interfaces
serverPort = 1658

# pan=3560562400007808
Resp1 = 'ISO0860000580310C22000000201801000000020080001001635605624000078080121090603'
Resp2 = '00076000BK1631000000000000000000000000000000000000000000000000000000000000000000090105890160000PRO200000000000000YY0000000000000000000000000000002046332042PATH35605630235605624058024014120120810000'
#ResHeader='\x01\x43'

#Open socket to listen on
sSock = socket(AF_INET, SOCK_STREAM)
sSock.bind((serverHost, serverPort))
sSock.listen(3)

#Handle connections
while 1:
    #Accept a connection
    conn, addr = sSock.accept()
    print 'Client Connection: ', addr
    while 1:

        #Receive data
        data = conn.recv(1024)
        if not data: break
        print 'Server Received: ', data
        traceNum = data[78:84]
        #       newData = data.replace('Client', 'Responsed')

        #Send response
        f = open('c:/trace.txt', 'w')
        x = hex(len(Resp1 + traceNum + Resp2))
        x.split('x')
        b = x[2:]
        header = '0000'
        header = header[:4 - len(b)] + b
        print 'xxxx:', header
        txt = binascii.a2b_hex(header) + Resp1 + traceNum + Resp2
        f.write(txt)
        conn.sendall(txt)
        print 'Server Reponse:', txt, ';Len:', len(txt)
        f.close()

#Close Connection
#   conn.close()

    
    
