from future import standard_library
standard_library.install_aliases()
from builtins import hex
# -*- coding: UTF-8 -*-
import socketserver
import time
import string
import binascii
import datetime

myHost = ''
myPort = 12343


def now():
    return time.ctime(time.time())


def trantime():
    trantime = time.strftime("%H%M%S", time.localtime())
    print trantime

    trandate = time.strftime("%m%d")
    print trandate

    date_ymd = time.strftime("%y%m%d")
    print date_ymd
    return (date_ymd, binascii.a2b_hex(trantime), binascii.a2b_hex(trandate))


class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print 'Welcome Clinet:', self.client_address
        while True:
            msg_in = self.request.recv(1024)
            time.sleep(1)
            if not msg_in: break

            #process bitmap data 
            def bitmap(msg):
                bitmap = (binascii.b2a_hex(msg[9:17]))
                bitmap_b2h = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', \
                              '0101': '5', '0110': '6', '0111': '7', '1000': '8', \
                              '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', \
                              '1110': 'e', '1111': 'f'}

                bitmap_h2b = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '1000', \
                              '5': '1001', '6': '1010', '7': '1011', '8': '1100', \
                              '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', \
                              'e': '1110', 'f': '1111'}

                #datatable ={1:[Fixed or Dynamic,Binary or Nible or Char, Max length]}
                ISO8583 = {1: ['f', 'b', 64], 2: ['d', 'n', 19], 3: ['f', 'n', '6'], 4: ['f', 'n', '12'], \
                           5: ['f', 'n', 12], 6: ['f', 'n', 12], 7: ['f', 'n', 10], 8: ['f', 'n', 8], \
                           9: ['f', 'n', 8], 10: ['f', 'n', 9], 11: ['f', 'n', 6], 12: ['f', 'n', 6], \
                           13: ['f', 'n', 4], 14: ['f', 'n', 4], 15: ['f', 'n', 4], 16: ['f', 'n', 4], \
                           17: ['f', 'n', 4], 18: ['f', 'n', 4], 19: ['f', 'n', 4], 20: ['f', 'n', 4], \
                           21: ['f', 'n', 4], 22: ['f', 'n', 4], 23: ['f', 'n', 4], 24: ['f', 'n', 4], \
                           25: ['f', 'n', 2], 26: ['f', 'n', 2], 27: ['f', 'n', 2], 28: ['f', 'n', 8], \
                           29: ['f', 'n', 8], 30: ['f', 'n', 8], 31: ['f', 'n', 4], 32: ['d', 'n', 12], \
                           33: ['d', 'n', 12], 34: ['d', 'n', 28], 35: ['d', 'z', 37], 36: ['d', 'n', 104], \
                           37: ['f', 'a', 12], 38: ['f', 'a', 6], 39: ['f', 'a', 2], 40: ['f', 'a', 3], \
                           41: ['f', 'a', 8], 42: ['f', 'a', 15], 43: ['f', 'a', 40], 44: ['d', 'a', 44], \
                           45: ['d', 'a', 76], 46: ['f', 'a', 999], 47: ['f', 'a', 999], 48: ['f', 'a', 999], \
                           49: ['f', 'a', 3], 50: ['f', 'a', 3], 51: ['f', 'a', 3], 52: ['f', 'b', 16], \
                           53: ['f', 'n', 18], 54: ['f', 'a', 120], 55: ['f', 'a', 999], 56: ['f', 'a', 999], \
                           57: ['f', 'a', 999], 58: ['f', 'a', 999], 59: ['f', 'a', 999], 60: ['f', 'a', 7], \
                           61: ['f', 'a', 999], 62: ['f', 'a', 999], 63: ['f', 'a', 999], 64: ['f', 'b', 16]}

                #解 Bitmap 
                bitmaplist = ''
                for item in bitmap:
                    bitmaplist = bitmaplist + bitmap_h2b[item]
                print 'BitMap 分解:', bitmaplist

            # process TPDU header 
            def tpdu(msg):
                tpdu_type = msg[2:3]
                tpdu_from = msg[3:5]
                tpdu_to = msg[5:7]
                tpdu = tpdu_type + tpdu_to + tpdu_from
                return tpdu

            #process message type and convert reponse message type
            def msgtype(msg):
                msgtype = (binascii.b2a_hex(msg[7:9]))
                if msgtype[2] == '0':
                    msgtype = msgtype[0:2] + '10'
                else:
                    msgtype = msgtype[0:2] + '30'
                return binascii.a2b_hex(msgtype)

            def mag(msg):

                #print now()                
                F3_processcode = msg[17:20]
                print 'F3:', binascii.b2a_hex(F3_processcode)
                F4_amt = msg[20:26]
                print 'F4:', binascii.b2a_hex(F4_amt)
                F11_traceno = msg[26:29]
                print 'F11_traceno:', binascii.b2a_hex(F11_traceno)
                F22_PosEntryMode = msg[29:31]
                print 'F22_PosEntryMode:', binascii.b2a_hex(F22_PosEntryMode)
                F24_NII = msg[31:33]
                print 'F24_NII:', binascii.b2a_hex(F24_NII)
                F25_PosConCode = msg[33:34]
                print 'F25_PosConCode:', binascii.b2a_hex(F25_PosConCode)
                F35_TrackII = msg[35:51]
                print 'F35_TrackII:', binascii.b2a_hex(F35_TrackII)
                F41_TID = msg[51:59]
                print 'F41_TID:', F41_TID
                F42_MID = msg[59:76]
                print 'F42_MID:', F42_MID, '\n'
                F48_data = msg[74:91]
                F48_PID = msg[76:91]
                print 'F48_PID:', F48_PID, '\n'

                tpdu_out = tpdu(msg)
                msgtype_out = msgtype(msg)
                bitmap_ok = binascii.a2b_hex('203801800e810000')
                F37_ymd, F12_trantime, F13_trandate = trantime()
                F37_rrn = F37_ymd + '000001'
                F38_authno = '013145'
                F39_resp = '00'
                msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                          + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                          + F37_rrn + F38_authno + F39_resp + F41_TID + F48_data
                return msg_txt


            #判斷是刷卡或人工
            msg_in_len = len(msg_in[2:])
            bitmap(msg_in)

            if msg_in_len == 0x004e:  #刷卡兌換
                print '#刷卡兌換'
                msg_out = mag(msg_in)
                print msg_out
            if msg_in == 0x0048:  #人工輸入卡號
                msg_out = manual(msg_in)

                #Compute len of message
            x = hex(len(msg_out))  #compute len of message
            x.split('x')  #0xaa ,
            b = x[2:]  #get aa
            header = '0000'
            header = header[:4 - len(b)] + b  # convert  TCPIP len of header

            txt = binascii.a2b_hex(header) + msg_out
            print 'Send Back:', binascii.b2a_hex(txt)
            self.request.send(txt)

        self.request.close()


myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
server.serve_forever()
