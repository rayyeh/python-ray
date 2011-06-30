from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *
import binascii

iso = ISO8583(debug=False)
iso.setMTI('0200')
iso.setBit(3,'000000')  
iso.setBit(4, '100')
iso.setBit(11, '100002')
iso.setBit(22, '021')
iso.setBit(24,'005')    
iso.setBit(25, '00')
iso.setBit(35, '4579522000000006D051250117440298000')
iso.setBit(41,'14100109')       
iso.setBit(42,'000100049900012')      
        
#Show bits
print 'Bits with values'
iso.showIsoBits()
iso.showBitmap()

#iso.showRawIso()
# Show raw ASCII ISO
print 'getRawISO -> ', binascii.b2a_hex(iso.getRawIso())
print 'showRawISO ->',iso.showRawIso()

#Show Network ISO        
tpdu='0700000010'
print 'getNetworkISO_POS :',  binascii.b2a_hex(iso.getNetworkISO_POS(tpdu))

exit()
