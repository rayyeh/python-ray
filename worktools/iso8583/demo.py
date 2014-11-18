from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *

iso = ISO8583()
iso.setMTI('0800')
iso.setBit(3, '300000')
iso.setBit(24, '045')
iso.setBit(41, '11111111')
iso.setBit(42, '222222222222222')
x = iso.getRawIso()
print "getRawIso =", x
y = iso.getBitmap()
print "getBitmap =", iso.getBitmap()
