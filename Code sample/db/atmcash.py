def connect():
    import socket
    import string
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    err =clientsocket.connect(('192.168.110.93',5008))
    if err <> 0:
        print err
    
    return clientsocket

def senddata(clientsocket):
    import binascii
    data='0114   4953   4F30   3136    3030   3030   3730   3032    3030   3332   3338   3830 3031   3238   4531   3930    3030   3031   3330   3030    3030   3030   3030   3230 \
    3030   3030   3130   3037    3032   3031   3331   3733    3936   3930   3130   3031 \
    3331   3130   3037   3130    3037   3036   3431   3239    3438   3337   3439   3431 \
    3336   3030   3136   3030    3031   3033   3D34   3931    3231   3231   3431   3233 \
    3438   3736   2020   2020    2031   3030   3737   3339    3639   3030   3038   3033 \
    3030   3138   3420   2020    2020   2020   2038   3033    3030   3136   3120   2020 \
    2020   2020   554E   494F    4E20   4241   4E4B   2020    2020   2020   2020   2020 \
    2020   5441   4950   4549    2043   4954   5920   2054    5720   5457   3034   3441 \
    2020   2020   2020   2020    2020   2020   2020   2020    2020   2020   2020   2034 \
    3030   3030   3031   3538    4120   2020   2020   2020    2020   2039   3031   4543     3431   3639   3530   3834    4234   3235   3843'                                     

    data1=data.split(' ') 
    data2=''.join(data1)    
    err =clientsocket.send(binascii.a2b_hex(data2))
    if err<>0 :
        print err            
    respdata=clientsocket.recv(1024)
    print respdata
    clientsocket.close()

def nac():
    s=connect()
    senddata(s)

if __name__ =='__main__':
   nac()