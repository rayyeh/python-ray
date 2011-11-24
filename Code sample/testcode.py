def connect():
    import socket
    import string
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    err =clientsocket.connect(('192.168.110.93',5020))
    if err <> 0:
        print err
    
    return clientsocket

def senddata(clientsocket):
    import binascii
    offline='00 66 60 01 50 80 \
    7C 02 20 70 3C 05 80 04 C0 00 0C 16 45 79 52 87 00 02 03 01 00 00 \
    00 00 00 00 00 01 00 00 01 24 \
    09 38 35 10 11 44 12 00 72 01 50 00 31\
    32 33 34 35 36 31 35 31 39 39 39 39 39 30 30 30 \
    31 30 30 30 35 30 34 30 30 30 32 37 00 15 20 20 \
    20 20 20 20 20 20 20 00 00 00 00 00 00 00 06 30 30 30 30 32 \
    33 20 '
    
    voidsale ='00 6F 60 01 50 80 \
    7C 02 00 70 3C 05 80 0C C0 00 14 16 45 79 52 87 00 02 03 01 02 00 \
    00 00 00 00 00 01 00 00 01 25 \
    09 38 23 10 11 44 12 00 12 01 50 00 35 \
    31 30 30 30 31 31 35 20 20 20 20 31 34 30 33 38 \
    39 31 35 31 39 39 39 39 39 30 30 30 31 30 30 30 \
    35 30 34 30 30 30 32 37 00 12 30 30 30 30 30 30 \
    30 30 30 31 30 30 00 06 30 30 30 30 32 34 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 \
    20 20 20 20 20 20 '

    offline1=offline.split(' ') 
    offline2=''.join(offline1)    
    #err =clientsocket.send(binascii.a2b_hex(offline2))
    
    voidsale1=voidsale.split(' ')
    voidsale2=''.join(voidsale1)
    clientsocket.send(binascii.a2b_hex(offline2))
    clientsocket.send(binascii.a2b_hex(voidsale2))
    
    #if err<>0 :
    #    print err            
    respdata=clientsocket.recv(1024)
    print respdata
    clientsocket.close()

def nac():
    s=connect()
    senddata(s)

if __name__ =='__main__':
   nac()