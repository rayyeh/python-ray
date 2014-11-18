def connect():
    import socket

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err = clientsocket.connect(('192.168.110.93', 5020))
    if err <> 0:
        print err

    return clientsocket


def senddata(clientsocket):
    import binascii

    data = '00 56 60 01 50 82 A5 01 00 70 24 05 80 00 C0 00 06 16 45 79 52 \
    490000 07 06 00 00 00 00 00 00 01 11 00 00 14 84 09 05 08 10 \
    015000 31 33 30 30 30 36 35 38 30 30 30 30 30 31 30 39 32 33 \
    303038 32 31 00 06 30 30 31 34 38 32 00 10 00 08 31 36 31 30 \
    203939 31'

    data1 = data.split(' ')
    data2 = ''.join(data1)
    err = clientsocket.send(binascii.a2b_hex(data2))
    if err <> 0:
        print err
    respdata = clientsocket.recv(1024)
    print respdata
    clientsocket.close()


def nac():
    s = connect()
    senddata(s)


if __name__ == '__main__':
    nac()