def connect():
    import socket

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = clientsocket.connect(('192.168.7.44', 5678))
    if err != 0:
        print("Connect error:",err)

    return clientsocket


def senddata(clientsocket):
    import binascii

#data = '00 56 60 01 50 82 A5 01 00 70 24 05 80 00 C0 00 06 16 45 79 52 \

    data = '01 00 70 24 05 80 00 C0 00 06 16 45 79 52 \
    490000 07 06 00 00 00 00 00 00 00 19 00 00 14 04 19 06 08 10 \
    015000 31 34 31 30 30 31 30 39 30 30 30 31 30 30 30 34 39 39 \
    303030 31 32 00 06 30 30 31 34 38 32 00 10 00 08 31 36 31 30 \
    303939 31'

    data1 = data.replace(' ','')
    #data2 = ''.join(data1)
    data3 =  binascii.a2b_hex(data1)
    print("Data3:",data3)
    err = clientsocket.sendall(data3)
    if err != 0:
        print("Sending error:",err)
    respdata = clientsocket.recv(1024)
    print(respdata)
    clientsocket.close()


def nac():
    s = connect()
    senddata(s)


if __name__ == '__main__':
    nac()
