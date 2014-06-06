'''  Batch auth for ONUS card
'''
from ISO8583_POS.ISO8583 import ISO8583
from ISO8583_POS.ISOErrors import *
from ISO8583_POS.ISO8583 import F63_Token
import socket
import sys
import time
import binascii


# Configure the client
serverIP = "192.168.110.93"
serverPort = 5020
timeBetweenEcho = 0  # in seconds
numberSEND = 10
MID='000100042300111'
TID='41000064'

# 4444444444444444444Dyymmsvrkpvvvcvv
PANLIST = {0:"4514458200782804D160820110831890000",
           1:"3560561500000309D160520110522289000"}
           #2:"49381700000000307D191210113150998000",
           #3:"49381700000000505D191210119882535000",}
PANLEN = len(PANLIST)
print ('PANLEN:', PANLEN)

bigEndian = True
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'socket error:', e
    s = None
try:
    s.connect((serverIP, serverPort))
except socket.error:
    s.close()
    s = None

if s is None:
    print  'Could not connect'
    sys.exit(1)

''' F63 field
F63data =F63_Token()
F63data.setCVV2(1,0,'147')
#F63data.setID('C220334664')
F63data.F63_value=F63data.setValue()
'''

for req in range(0, numberSEND):
    traceno = 100000 + req
    iso = ISO8583(debug=False)
    iso.setMTI('0100')
    #        iso.setBit(2,'4514458700052708')
    iso.setBit(3, '000000')
    iso.setBit(4, '100')
    iso.setBit(11, traceno)
    #        iso.setBit(14,'2912')
    iso.setBit(22, '010')
    iso.setBit(24, '005')
    iso.setBit(25, '00')
    if  req == 0: x = 0
    else:  x = (req % PANLEN)

    print ('x:%d  ,PAN:%s' % (x, PANLIST[x]))
    iso.setBit(35, PANLIST[x])
    iso.setBit(41, TID)
    iso.setBit(42, MID)
    #iso.setBit(63,F63data.F63_value)

    tpdu = '7000000010'

    #Show bits
   # print 'Show Bits with values\n', iso.showIsoBits()

    # Show raw ASCII ISO
    #print 'The package is -> '
    #iso.showRawIso()

    try:
        if bigEndian:
            message = iso.getNetworkISO_POS(tpdu)
        else:
            message = iso.getNetworkISO_POS(tpdu, False)
        print 'Requesting ... %s' % binascii.b2a_hex(message)

        try:
            err = s.send(message)
        except socket.error, err:
            print 'sending error:', err

        ans = s.recv(2048)
        print "\nResponse....: \n%s|" % binascii.b2a_hex(ans)
        isoAns = ISO8583()

        if bigEndian:
            isoAns.setNetworkISO_POS(ans)
        else:
            isoAns.setNetworkISO_POS(ans, False)
        '''
        MTI = isoAns.getMTI()
        print "MTI value =", MTI

        v1 = isoAns.getBitsAndValues()
        for v in v1:
            print 'Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value'])
            '''

    except InvalidIso8583, ii:
        print ii
        break

    print 'Send %s times' % (req + 1)
    time.sleep(timeBetweenEcho)

print 'Closing...'
s.close()               
