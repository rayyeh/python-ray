import binascii
import socket
import sys
import time

DEBUG_ON = 0


class HSM(object):
    ZMK = 'C77A58BAD7EE39E2FAC5AE02A2A7DB2E'
    ZPK = 'U914FCB221A02829D914FCB221A02829D'
    ZPK_ZMK = 'X9DB32983809C188C9DB32983809C188C'
    PVK = '3B3A0EC90E9C558B3B3A0EC90E9C558B'
    CVK = '29A34CB42019217B4D7487DE72C779AD'
    MDK = 'UB296E1B08A8E292E8E26512F69904163'

    PIN_Block_LMK = ''
    PVV = ''
    PIN = "1234"
    pan = '4579520612345702'
    expire_date = '4902'
    CVV = ''
    Resp = ''
    PIN_Block_ZPK = ''
    PIN_Block_TPK = ''

    output = ''
    sock = socket.socket

    serverIP = "192.168.110.180"
    serverPort = 1500

    def _testconnect(self):
        if not isinstance(self.sock, socket.socket):
            self.output = '%sPlease connect HSM First\n' % (self.output)
            return False
        else:
            return True


    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, e:
            print  'socket error:', e
            self.output = 'socket error:', e
            self.sock = None

        try:
            self.output = '%sConnecting... %s\n' % (self.output, self.serverIP)
            print 'Connecting..%s\n' % (self.serverIP)
            print ' serverip:%s serverport %s' % (type(self.serverIP) \
                                                      , type(self.serverPort))

            self.sock.connect((self.serverIP, self.serverPort))
            print 'Connected-> %s\n' % (self.serverIP)
            self.output = '%sConnected-> %s\n' % (self.output, self.serverIP)
        except socket.error:
            self.sock.close()
            self.sock = None

        if self.sock is None:
            print  'Could not connect'
            self.output = '%sCould not connect.\n' % (self.output)

    def close(self):
        print 'Closing ....', self.serverIP
        self.sock.close()
        self.output = '%sClosing-> %s\n' % (self.output, self.serverIP)

    def ARQC(self):
        if self._testconnect():
            func = "Verify ARQC and Generate ARPC,"
            msg_header = '0001'
            command_code = 'KQ'
            chipdata1 = '795287000203010002160C516338323800000000010000000000000001'
            chipdata2 = '5880800080000901110525000C5163381800021603A00000'
            chipdata3 = '0000003BD2E032C8948E55A5303000'
            # data =msg_header+command_code+"10"+self.MDK+binascii.a2b_hex(chipdata1+chipdata2+chipdata3)
            #data=msg_header+"A8"+"002"+"U5FDAA193A2324BA1CB789D8C93824871"+"84A24A12E2A48F24"+"Z"
            data1 = msg_header + "CC" + "U2CFDF85580B3722AD14B412CE64FDC80"
            data2 = 'UF52A84937BC7FA6F389A7B74BFF3170C12F955E5A5341172200101233300070511'
            data = data1 + data2
            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            print message
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.output = '%sVerify ARQC and Genrate ARPC,return-code:%s, ARPC:%s\n' \
                          % (self.output, self.Resp[2:10], str.upper(binascii.b2a_hex(self.Resp[10:18])))
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]


if __name__ == '__main__':
    hsm = HSM()
    hsm.connect()
    print 'Begin Stress Test'
    start = time.time()

    for i in range(1, 3001):
        hsm.ARQC()
    print 'Total spend time:', (time.time() - start)
    hsm.close()
    print 'Stress Test End\n'
    
    
