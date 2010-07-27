#######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#'*60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#'*60

import thread
import sys,time,os
from socket import *
        
def client(id):
        serverHost = '192.168.110.93'
        serverPort = 12343    
        
        def now():
                return time.ctime(time.time( ))

        message = 'I am ID: %s' %id + '- Time: %s' %(now())   

        if len(sys.argv) > 1:
                serverHost = sys.argv[1]
                
        #Create a socket                
        sSock = socket(AF_INET, SOCK_STREAM)                        
        
        try :
            #Connect to server
            sSock.connect((serverHost, serverPort))
        except Exception, e:
            sSock.close()
            os._exit(0)
        
        #Send messages
        sSock.send(message)        
        data = sSock.recv(1024)
        print 'Client %s received: ' %id, data
        sSock.close()   
        os._exit(0)

def main():
        i=0         
        while True:
			newpid = os.fork()
			if newpid == 0:client(i)
			i=i+1
			if i > 10 :break
				

if __name__ =='__main__':
        main()
        


