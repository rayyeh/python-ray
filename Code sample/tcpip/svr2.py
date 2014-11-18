# ######################################################
# # Demo:Receiving Streaming Data Using the ServerSocket Module
#######################################################
print '#' * 60
print '# Demo:Receiving Streaming Data Using the ServerSocket Module'
print '#' * 60

import socket
import string
import SocketServer


class myTCPServer(SocketServer.StreamRequestHandler):
    def handle(self):
        while 1:
            peer = self.connection.getpeername()[0]
            line = self.rfile.readline()  #Read streaming data
            print "%s wrote: %s" % (peer, line)
            sck = self.connection.getsockname()[0]

            #send data back to the client from the streaming server
            self.wfile.write("%s: %d bytes successfuly received." % (sck, len(line)))

            #Create SocketServer object


serv = SocketServer.TCPServer(("", 50007), myTCPServer)

#Activate the server to handle clients
serv.serve_forever()

