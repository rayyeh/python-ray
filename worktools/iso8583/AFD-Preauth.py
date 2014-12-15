'''
pos1.py  import  import F63_Token
'''
from builtins import range
import socket
import sys
import time
import binascii

from ISO8583_POS.ISO8583 import ISO8583
from ISO8583_POS.ISOErrors import *
from ISO8583_POS.ISO8583 import F63_Token



# Configure the client
serverIP = "192.168.110.93"
serverPort = 5020
numberEcho = 1
timeBetweenEcho = 0  # in seconds

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

F63data = F63_Token()
F63data.setCVV2(1, 0, '147')
# F63data.setID('C220334664')
F63data.F63_value = F63data.setValue()

for req in range(0, numberEcho):
    traceno = 500001 + req
    iso = ISO8583(debug=False)
    iso.setMTI('0100')
    iso.setBit(2, '4514458700052708')
    iso.setBit(3, '300000')
    iso.setBit(4, '100')
    iso.setBit(11, traceno)
    iso.setBit(14, '2912')
    iso.setBit(22, '810')
    iso.setBit(24, '005')
    iso.setBit(25, '00')
    #iso.setBit(35, '4579522000000006D440710117440298000')
    iso.setBit(41, '74000711')
    iso.setBit(42, '000100413200072')
    iso.setBit(63, F63data.F63_value)

    tpdu = '7000000010'

    #Show bits
    print 'Show Bits with values\n', iso.showIsoBits()

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

        MTI = isoAns.getMTI()
        print "MTI value =", MTI

        v1 = isoAns.getBitsAndValues()
        for v in v1:
            print 'Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value'])

    except InvalidIso8583, ii:
        print ii
        break

    print 'Send %s times' % (req + 1)
    time.sleep(timeBetweenEcho)

print 'Closing...'
s.close()               
