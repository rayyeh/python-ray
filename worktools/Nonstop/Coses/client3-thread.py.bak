# -*- coding:utf-8 -*-
# ######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#' * 60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#' * 60

import thread
import sys
import time
from socket import *


def client(id):
    serverHost = '127.0.0.1'
    serverPort = 22222

    def now():
        return time.ctime(time.time())

    message = 'I am ID: %s  Time: %s \n' % ( id, now())

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
        thread.exit()

    #Send messages
    print 'Client send  => %s \n' % (message)
    sSock.send(message)
    data = sSock.recv(1024)
    print 'Client received <= %s\n ' % (data)
    sSock.close()
    thread.exit()


def main():
    i = 0
    while True:
        thread.start_new_thread(client, (i, ))
        i = i + 1
        if i > 20:
            break
    print 'Already send MAX client  %s thread\n' % i


if __name__ == '__main__':
    main()
        


