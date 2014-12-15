from future import standard_library
standard_library.install_aliases()
from builtins import hex
# ######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#' * 60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#' * 60

import _thread
import sys
import time
from socket import *
import binascii


def client(id):
    serverHost = '192.168.110.1'
    serverPort = 1234

    def now():
        return time.ctime(time.time())

    messagedata = 'I am ID: %s' % id
    x = hex(len(messagedata))
    x.split('x')
    b = x[2:]
    header = '0000'
    header = header[:4 - len(b)] + b
    message = binascii.a2b_hex(header) + messagedata

    if len(sys.argv) > 1:
        serverHost = sys.argv[1]

    #Create a socket
    sSock = socket(AF_INET, SOCK_STREAM)

    try:
        #Connect to server
        sSock.connect((serverHost, serverPort))
    except Ioexception, e:
        print 'Can  not connect', e
        sSock.close()
        _thread.exit()

    #Send messages
    sSock.send(message)
    data = sSock.recv(1024)
    print 'Client received: ', data
    sSock.close()
    _thread.exit()


def main():
    i = 0
    while True:
        _thread.start_new_thread(client, (i, ))
        i = i + 1
        if i > 100: break


if __name__ == '__main__':
    main()
        


