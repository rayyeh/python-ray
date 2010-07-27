from ISO8583_POS.ISO8583 import ISO8583
from ISO8583_POS.ISOErrors import *
import socket 
import sys
import time
import binascii


# Configure the client
serverIP = "192.168.110.93" 
serverPort = 5030
numberEcho = 1
timeBetweenEcho = 5 # in seconds

bigEndian = True
#bigEndian = False

s = None
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, e:
    print 'socket error:',  e
    s = None

try:
    s.connect((serverIP, serverPort))
except socket.error:
    s.close()
    s = None    

if s is None:
    print  'Could not connect'
    sys.exit(1)

################################################################################
F63 = {}
def setVbv(eci,cavv,xid):
    '''# Tag Visa VbV '''
    tag='99'
    size=binascii.a2b_hex('0043')
    value=size+eci+binascii.a2b_hex(cavv)+binascii.a2b_hex(xid)
    tsize= 45
    F63[tag]=[tsize,size,value]
    return F63
################################################################################
def setID(id):
    ''' # Tag ID checking'''
    tag='ID'
    size=binascii.a2b_hex('0012')
    value=size+tag+id.upper()
    tsize=14
    F63[tag]=[tsize,size,value]
    return F63



def setCVV2(ind,resp,cvv):
    ''' # Tag CVV2'''
    tag='16'
    size=binascii.a2b_hex('0008')
    value =size+tag+str(ind)+str(resp)+cvv.rjust(4,' ')
    tsize=10
    F63[tag]=[tsize,size,value]
    return F63



def setUCAF(ucaf,ucaf_len,ucaf_value):
    ''' # Tag MasterCard UCAF'''
    tag='98'
    size=binascii.a2b_hex('0037')
    value=size+tag+ucaf_len+ucaf_value
    tsize=39
    F63[tag]=[tsize,size,value]
    return 63



def setBirthday(birthday):
    ''' # Tag Birthday'''
    tag='97'
    size=binsacii.a2b_hex('0010')
    value=size+tag+birthday
    tsize=12
    F63[tag]=[tsize,size,value]
    return 63


def setHostRep():
    '''# Tag Host Response message '''
    tag='31'
    size=binsacii.a2b_hex('0005')
    value=size+tag+'   '
    tsize=7
    F63[tag]=[tsize,size,value]
    return F63



def setFund(tx,product):
    ''' Tag Fund  : tx =F, product = fund product code'''
    tag='U2'
    size=binascii.a2b_hex('0005')
    value=size+tag+tx+product
    tsize=7
    F63[tag]=[tsize,size,value]
    return F63


 # Tag 'U1', EDC function cod flag ,bitcode = 2 bytes, HEX value 
def setEDCFun(bitcode):
    tag='U1'
    size=binascii.a2b_hex('0003')
    value=size+tag+binascii.a2b_hex(bitcode.upper(bitcode))
    tsize=5
    F63[tag]=[tsize,size,value]
    return F63

# CUP txn #
def setCUP(traceno,settle_date,transmit_date,transmit_time,rrn):
    ''' # CUP txn'''
    tag='CU'
    size=binascii.a2b_hex('0034')
    value=size+tag+traceno+settle_date+transmit_date+transmit_time+rrn
    tsize=36
    F[63]=[tsize,size,value]
    return F63


F63=setCVV2(1,0,'147')
F63=setID('C220334664')
i=F63_size=0
F63_value=''
for i in F63:
    F63_size  += F63[i][0]
    F63_value += F63[i][2]
################################################################################


for req in range(0,numberEcho):
        
        iso = ISO8583(debug=False)
        iso.setMTI('0200')
        iso.setBit(2,'4579520612345702')
        iso.setBit(3,'000000')
        iso.setBit(4, '100')
        iso.setBit(11, '100018')
        iso.setBit(14,'4902')
        iso.setBit(22, '810')
        iso.setBit(24,'005')
        iso.setBit(25, '00')
        #iso.setBit(35, '4579522000000006D440710117440298000')
        iso.setBit(41,'14100109')
        iso.setBit(42,'000100049900012')
        iso.setBit(63,F63_value)
        
        tpdu='7000000010'
        
        #Show bits
        print 'Bits with values\n', iso.showIsoBits()
        
        # Show raw ASCII ISO
        #print 'The package is -> '
        #iso.showRawIso()        
        
        try:
            if bigEndian:
                message = iso.getNetworkISO_POS(tpdu)
            else:
                message = iso.getNetworkISO_POS(tpdu, False)
            
            print 'Requesting ... %s'   % binascii.b2a_hex(message)
            
            try :
                err=s.send(message)
            except socket.error, err:
                print 'sending error:', err                
            
            ans = s.recv(2048)
            print "\nResponse....: \n%s|" % binascii.b2a_hex(ans)
            isoAns = ISO8583()
            
            if bigEndian:
                isoAns.setNetworkISO_POS(ans)
            else:
                isoAns.setNetworkISO_POS(ans, False)
                
            MTI=isoAns.getMTI()
            print "MTI value =",   MTI
                
            v1 = isoAns.getBitsAndValues()
            for v in v1:
                print 'Bit %s of type %s with value = %s' % (v['bit'],v['type'],v['value'])
                                
                                          
        except InvalidIso8583, ii:
                print ii
                break               

        time.sleep(timeBetweenEcho)               
                
print 'Closing...'              
s.close()               
