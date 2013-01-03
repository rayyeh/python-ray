import zmq
import sys

#Provide two ports of two different servers to connect to simultaneously
port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

#Client is created with a socket type “zmq.REQ”. You should notice that the same socket can connect to
#two different servers
context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

#You have to send a request and then wait for reply.
#  Do 10 requests, waiting each time for a response
for request in range(1, 20):
    print "Sending request ", request, "..."
    socket.send("Hello1")
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
