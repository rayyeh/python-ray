#############################################################################
# Server side: open a socket on a port, listen for a message from a client,
# and send an echo reply; this version uses the standard library module
# SocketServer to do its work; SocketServer allows us to make a simple
# TCPServer, a ThreadingTCPServer, a ForkingTCPServer, and more, and
# routes each client connect request to a new instance of a passed-in
# request handler object's handle method; SocketServer also supports
# UDP and Unix domain sockets; see the library manual for other usage.
#############################################################################


# coding TCPIP using ThreadingTCPServer  method
import SocketServer, time               # get socket server, handler objects
HOST = ''                             # server machine, '' means local host
PORT = 50002                          # listen on a non-reserved port number
def now( ):
    return time.ctime(time.time( ))

class MyClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):                           # on each client connect
        print self.client_address, now( )            # show this client's address
        time.sleep(1)                           # simulate a blocking activity
        while True:                             # self.request is client socket
            data = self.request.recv(1024)      # read, write a client socket
            if not data: break
            print 'Receving msg: %s' %(data)
            self.request.send('%s at %s' % (data, now( )))
        self.request.close( )

    


if  __name__ == '__main__':
    Host=raw_input('Typing your server ip:\n')
    PORT_raw=raw_input('Typing your server port:\n')
    if PORT_raw !='':
        PORT = int(PORT_raw)  
    myaddr = (HOST, PORT)
    server = SocketServer.ThreadingTCPServer(myaddr, MyClientHandler)
    print 'Server-class Staring ip:%s, port:%s \n' %(HOST,PORT)
    server.serve_forever( )

