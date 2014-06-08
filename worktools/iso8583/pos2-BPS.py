'''
pos2.py  import  import F63_Token
set socket  non-blocking,it  open and connect COSES POS  PI.
  send  serveral iso8583 request to POS PI.
  use while Tru loop to get recponse from POS PI.
'''

from ISO8583_POS.ISO8583 import ISO8583
from ISO8583_POS.ISOErrors import *
from ISO8583_POS.ISO8583 import F63_Token
import socket 
import sys
import time
import binascii,errno


# Configure the client
serverIP = "127.0.0.1" 
serverPort = 5000
timeBetweenEcho = 0.2 # in seconds
bigEndian = True
s = None
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, e:
    print 'socket error:',  e
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

#F63data =F63_Token()
#F63data.setCVV2(1,0,'147')
#F63data.setID('C220334664')
#F63data.F63_value=F63data.setValue()

class TRAN1:
    def __init__(self, pan):
        self.pan = pan
        self.traceno = '000001'
        self.iso=ISO8583(debug=False)
        self.iso.setMTI('0100')
        self.iso.setBit(2,self.pan)
        self.iso.setBit(3,'000000')
        self.iso.setBit(4, '100')
        self.iso.setBit(11, self.traceno)
        self.iso.setBit(14,'1912')
        self.iso.setBit(22, '810')
        self.iso.setBit(24,'005')
        self.iso.setBit(25, '00')
        #iso.setBit(35, '4579522000000006D440710117440298000')
        self.iso.setBit(41,'41000064')
        self.iso.setBit(42,'000100042300111')
        #iso.setBit(63,F63data.F63_value)
        self.tpdu='7000000010'
        #Show bits
        #print 'Show Bits with values\n', iso.showIsoBits()
    
class TRAN2:
    def __init__(self,pan):
        self.pan = pan
        self.traceno='000001'
        self.iso = ISO8583(debug=False)
        self.iso.setMTI('0100')
        self.iso.setBit(2,self.pan)
        self.iso.setBit(3,'000000')
        self.iso.setBit(4, '100')
        self.iso.setBit(11, self.traceno)
        self.iso.setBit(14,'1812')
        self.iso.setBit(22, '810')
        self.iso.setBit(24,'005')
        self.iso.setBit(25, '00')
        #self.iso.setBit(35, '4579522000000006D440710117440298000')
        self.iso.setBit(41,'74000126')
        self.iso.setBit(42,'000100203200050')
        #self.iso.setBit(63,F63data.F63_value)
        self.tpdu='7000000010'
        #Show bits
        #print 'Show Bits with values\n', iso.showIsoBits()

class TRAN3:
    def __init__(self,pan):
        self.pan = pan
        self.traceno='000001'
        self.iso = ISO8583(debug=False)
        self.iso.setMTI('0100')
        self.iso.setBit(2,self.pan)
        self.iso.setBit(3,'000000')
        self.iso.setBit(4, '100')
        self.iso.setBit(11, self.traceno)
        self.iso.setBit(14,'1912')
        self.iso.setBit(22, '810')
        self.iso.setBit(24,'005')
        self.iso.setBit(25, '00')
        #self.iso.setBit(35, '4579522000000006D440710117440298000')
        self.iso.setBit(41,'74005960')
        self.iso.setBit(42,'000100313200016')
        #self.iso.setBit(63,F63data.F63_value)
        self.tpdu='7000000010'
        #Show bits
        #print 'Show Bits with values\n', iso.showIsoBits()

t1= TRAN1('4938170000000018')
t2= TRAN2('5430450000000014')
t3= TRAN3('4938170000000505')
transet =[t1,t2,t3]
traceno= 0
numberSEND=1
cnt=0

for req in range(numberSEND):
    for t in transet:
        traceno=traceno+1
        t.iso.setBit(11, traceno)
        if bigEndian:
            tran_message = t.iso.getNetworkISO_POS(t.tpdu)
        else:
            tran_message = t.iso.getNetworkISO_POS(t.tpdu, False)
        try :
            err=s.send(tran_message)
        except socket.error, err:
            print 'sending error:', err
        print "** Sending  Transeq %d: %s"  % (traceno,binascii.b2a_hex(tran_message))
        time.sleep(timeBetweenEcho)
    try:
        ans = s.recv(2048)
        if not ans:
            print "connection closed"
            sock.close()
            break
        else:
            print "Received Bulk %d bytes: %s" % (len(ans), binascii.b2a_hex(ans))
            datarecv=[]
            startloc=0
            msg_count =0
            while startloc < len(ans):
                msg_len=str(binascii.b2a_hex(ans[startloc:startloc+2]))
                data_h=msg_len.lstrip('0')
                data_len = int(data_h,16)
                data_len = data_len+2
                data=ans[startloc:startloc+data_len]
                datarecv.append(binascii.b2a_hex(data))
                startloc=startloc+data_len
                msg_count =msg_count + 1                

            for item in datarecv:                
                cnt = cnt +1 
                print '** Received-%d:%s ' %(cnt,item)

    except socket.error, e:
        if e.args[0] == errno.EWOULDBLOCK:
            print 'EWOULDBLOCK'
            time.sleep(1)           # short delay, no tight loops
        else:
            print e
            break


