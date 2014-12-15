from future import standard_library
standard_library.install_aliases()
# ############################################################################
# Server side: open a socket on a port, listen for a message from a client,
# and send an echo reply; echoes lines until eof when client closes socket;
# spawns a thread to handle each client connection; threads share global
# memory space with main thread; this is more portable than fork: threads
# work on standard Windows systems, but process forks do not;
# ############################################################################

import _thread, time
from socket import *  # get socket constructor and constants

myHost = '127.0.0.1'  # server machine, '' means local host
myPort = 50010  # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)  # make a TCP socket object
sockobj.bind((myHost, myPort))  # bind it to server port number
sockobj.listen(5)  # allow up to 5 pending connects


def now():
    return time.ctime(time.time())  # current time on the server


def handleClient(connection):  # in spawned thread: reply
    time.sleep(1)  # simulate a blocking activity
    while True:  # read, write a client socket
        data = connection.recv(1024)
        print 'Receving msg: %s' % (data)
        if not data: break
        connection.send('%s at %s' % (data, now()))
    connection.close()


def dispatcher():  # listen until process killed
    while True:
        # wait for next connection,
        connection, address = sockobj.accept()  # pass to thread for service
        print 'Server connected by', address,
        print 'at', now()
        _thread.start_new(handleClient, (connection,))


print 'Server-Threading staring\n'
dispatcher()

