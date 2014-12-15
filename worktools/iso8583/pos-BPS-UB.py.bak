'''
1.Socket  non-blocking,it  open and connect COSES POS  PI.
2.UB test card tables
'''

import socket
import sys
import time
import binascii
import errno

from ISO8583_POS.ISO8583 import ISO8583




# Configure the client
serverIP = "192.168.110.93"
serverPort = 5000
timeBetweenEcho = 0.2  # in seconds
bigEndian = True
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'socket error:', e
    s = None
try:
    s.connect((serverIP, serverPort))
    s.setblocking(0)
except socket.error:
    s.close()
    s = None
if s is None:
    print  'Could not connect'
    sys.exit(1)

# F63data =F63_Token()
# F63data.setCVV2(1,0,'147')
# F63data.setID('C220334664')
# F63data.F63_value=F63data.setValue()

class TRAN:
    def __init__(self, pan, tid, mid):
        self.pan = pan
        self.tid = tid
        self.mid = mid
        self.traceno = '000001'
        self.iso = ISO8583(debug=False)
        self.iso.setMTI('0100')
        #self.iso.setBit(2, self.pan)
        self.iso.setBit(3, '000000')
        self.iso.setBit(4, '100')
        self.iso.setBit(11, self.traceno)
        #self.iso.setBit(14, '1912')
        self.iso.setBit(22, '901')
        self.iso.setBit(24, '005')
        self.iso.setBit(25, '00')
        self.iso.setBit(35, self.pan)
        self.iso.setBit(41, self.tid)
        self.iso.setBit(42, self.mid)
        #iso.setBit(63,F63data.F63_value)
        self.tpdu = '7000000010'
        #Show bits
        #print 'Show Bits with values\n', iso.showIsoBits()


''' test PAN table'''
PANDICT = {0: "4514458200782804D160820110831890000",
           1: "3560561500000309D160520110522443000",
           2: "3560568200000604D160520116908289000",
           3: "4579528700020301D441220111635324000",
           4: "5237642400001007D160820116286136000"}

''' Test MER/TID  table '''
MER = {0: {"tid": "41000064", "mid": '000100042300111'},
       1: {"tid": "74000126", "mid": "000100203200050"},
       2: {"tid": "74005960", "mid": "000100313200016"}}

t0 = TRAN('0', MER[0]["tid"], MER[0]["mid"])
t1 = TRAN('1', MER[1]["tid"], MER[1]["mid"])
t2 = TRAN('2', MER[2]["tid"], MER[2]["mid"])
transet = [t0, t1, t2]
traceno = 0
numberSEND = 2
cnt = 0

for req in range(numberSEND):
    for t in transet:
        if req == 0:
            x = transet.index(t) % len(PANDICT)
        else:
            x = ( req * len(transet) + transet.index(t)) % len(PANDICT)
        print ("REQ:%d,TRAN_INDEX:%d,PAN_INDEX:%d" % (req, transet.index(t), x))

        t.iso.setBit(35, PANDICT[x])
        t.iso.setBit(11, int(t.traceno) + req)
        print 'Show Bits with values\n', t.iso.showIsoBits()

        if bigEndian:
            tran_message = t.iso.getNetworkISO_POS(t.tpdu)
        else:
            tran_message = t.iso.getNetworkISO_POS(t.tpdu, False)
        try:
            err = s.send(tran_message)
        except socket.error, err:
            print 'sending error:', err
        print "** Sending  Transeq %d: %s" % (traceno, binascii.b2a_hex(tran_message))
        time.sleep(timeBetweenEcho)
    try:
        ans = s.recv(2048)
        if not ans:
            print "connection closed"
            s.close()
            break
        else:
            print "Received Bulk %d bytes: %s" % (len(ans), binascii.b2a_hex(ans))
            datarecv = []
            startloc = 0
            msg_count = 0
            while startloc < len(ans):
                msg_len = str(binascii.b2a_hex(ans[startloc:startloc + 2]))
                data_h = msg_len.lstrip('0')
                data_len = int(data_h, 16)
                data_len = data_len + 2
                data = ans[startloc:startloc + data_len]
                datarecv.append(binascii.b2a_hex(data))
                startloc = startloc + data_len
                msg_count = msg_count + 1

            for item in datarecv:
                cnt = cnt + 1
                print '** Received-%d:%s ' % (cnt, item)

    except socket.error, e:
        if e.args[0] == errno.EWOULDBLOCK:
            print 'EWOULDBLOCK'
            time.sleep(1)  # short delay, no tight loops
        else:
            print e
            break


