#######################################################
## Demo:Opening a Server-Side Socket for Receiving Data
#######################################################
print '#'*60
print '# Demo:Opening a Server-Side Socket for Receiving Data'
print '#'*60

from socket import *
import binascii

serverHost = '' # listen on all interfaces
serverPort = 1600

"""
ISO0860000510300C22000000001801000000020080000001654096636037520080708074552289303
076000BK1631000000000000000000000000000000000000000000000000000000000000000000090105890160000PRO200000000000000YY000000000000000000000000000000502NF

ISO0860000510310C22000000201801000000020080001001654096636037520080708074552
076000BK1631000000000000000000000000000000000000000000000000000000000000000000090105890160000PRO200000000000000YY000000000000000000000000000000502NF150000000000000000
'''"""

#07/08/2009 15:45:53.239253
# pan=3560562400007808
INQ1='ISO0860000510310C22000000201801000000020080001001645795206123457020917074552'
INQ2='076000BK1631000000000000000000000000000000000000000000000000000000000000000000090105890160000PRO200000000000000YY000000000000000000000000000000502NF150'

ADD1='ISO0860000510310C22000000201801000000020080001001645795206123457020917074552'
ADD2='076000BK1631000000000000000000000000000000000000000000000000000000000000000000090105890160000PRO200000000000000YY000000000000000000000000000000502NF015'

#ResHeader='\x01\x43'

#Open socket to listen on
sSock = socket(AF_INET, SOCK_STREAM)
sSock.bind((serverHost, serverPort))
sSock.listen(3)
db={}

#Handle connections
while 1:
#Accept a connection
    conn, addr = sSock.accept()
    print 'Client Connection: ', addr
    while 1:

#Receive data
        data = conn.recv(1024)
        if not data: break
        #print 'trace-num',data[70:90]
        traceNum=data[78:84]        

#Send response      
        if data[227:228] == '5':
            pan=data[52:68]
            print 'INQUIRE:',pan            
            if db.has_key(pan) :
                s120=db[pan]
                F38='00'
            else:
                F38='N6'
                s120='0'*15
            print 'pan:',pan,' S120:',s120,' F38:',F38
            x=hex(len(INQ1+traceNum+F38+INQ2+s120))
            x.split('x')
            b=x[2:]
            header='0000'
            header=header[:4-len(b)]+b
            txt=binascii.a2b_hex(header)+INQ1+traceNum+F38+INQ2+s120
        elif data[227:228] == '1' or data[227:228] == '2':
            pan=data[52:68]
            print 'ADD/UPDATE:',pan
            if db.has_key(pan):
                s120=data[235:]
                db[pan]=s120
            else:
                s120=data[235:]
                db[pan]=s120
            F38='00'
            print 'pan:',pan,'S120:',s120,'F38:',F38
            x=hex(len(ADD1+traceNum+F38+ADD2+s120))
            x.split('x')
            b=x[2:]
            header='0000'
            header=header[:4-len(b)]+b
            txt=binascii.a2b_hex(header)+ADD1+traceNum+F38+ADD2+s120
        elif data[227:228] == '3':
            pan=data[52:68]
            print 'Delete:',pan
            if db.has_key(pan) :
                db[pan]='0'*15
                s120='0'*15
                del db[pan]
                F38='00'
            else:
                db[pan]='0'*15
                s120='0'*15
                F38='25'
            print 'pan:',pan,'S120:',s120,'F38:',F38
            x=hex(len(INQ1+traceNum+F38+INQ2+s120))
            x.split('x')
            b=x[2:]
            header='0000'
            header=header[:4-len(b)]+b
            txt=binascii.a2b_hex(header)+INQ1+traceNum+F38+INQ2+s120
            

        conn.sendall(txt)
        
       

#Close Connection
#   conn.close()

    
    
