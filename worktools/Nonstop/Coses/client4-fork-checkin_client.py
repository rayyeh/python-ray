#######################################################
## Demo:Opening a Client-Side Socket for Sending Data
#######################################################
print '#'*60
print '# Demo:Opening a Client-Side Socket for Sending Data'
print '#'*60

import thread
import sys,time,os,binascii
from socket import *
        
def client(id):
                
        serverHost = '192.168.110.79'
        serverPort = 12343
        
        def now():
                return time.ctime(time.time( ))        

        if len(sys.argv) > 1:
                serverHost = sys.argv[1]
                
        #Create a socket                
        sSock = socket(AF_INET, SOCK_STREAM) 
                
        #message = 'I am ID: %s' %id + '- Time: %s' %(now())   
                
                
        data="00 4e 60 01 12 00 00 01 00 30 20 05 80 20 c1 00 00 00 \
        08 80 00 00 00 00 00 00 00 00 25 00 22 01 12 43 32 42 13 78 \
        88 50 00 83 89 d1 11 22 21 17 68 69 18 30 38 30 38 32 39 30 \
        36 32 30 30 38 30 38 32 39 30 30 30 30 30 30 31 00 04 31 32 36 30"
                
        data1=''
        data1=data.split(' ') 
        message=''.join(data1)                      
        
        try :
            #Connect to server
            sSock.connect((serverHost, serverPort))
        except Exception, e:
            sSock.close()
            os._exit(0)
        
        #Send messages
        sSock.send(binascii.a2b_hex(message))        
        #sSock.send(message) 
        data = sSock.recv(1024)
        print 'Client %s received: '%id, binascii.b2a_hex(data)
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
        


