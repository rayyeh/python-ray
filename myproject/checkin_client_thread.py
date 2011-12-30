#-*- coding:utf-8 -*-

import thread,time

def test(id,F11):
    #print 'I am id:%s,tranno:%s,' %(id,F11)
    import socket
    import string
    import binascii
    tranno=''
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsocket.setblocking(1)
    try:
        err=clientsocket.connect(('127.0.0.1',5051))
    except Exception,err:
        print 'Connect error :', err  
        
    tranno=str((int(id)+int(F11)))
    tranno=tranno.rjust(6,'0')
    print 'I am id:%s,tranno:%s,' %(id,tranno)
        
    
    tid='3038303832393036'    
    data1='004e600112000001003020058020c10000000880000000000000'    
    data2='0022011243324213788850008389d111222117686918'    
    data3='323030383038323930303030303031000431323630'
        
    data2=data1+tranno+data2+tid+data3 
        
    try:
        err=clientsocket.send(binascii.a2b_hex(data2))
    except Exception,err:
        print 'Sending err:',err
    
    try:      
        respdata=clientsocket.recv(1024)
    except Exception,err:
        print 'Receving err:',err
        
    print 'Receving:',binascii.b2a_hex(respdata)
    clientsocket.close()    

if __name__ =='__main__':
    for i in range(100):
        startF11=1
        thread.start_new_thread(test,(i,startF11))
        time.sleep(0.5)
