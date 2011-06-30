from pyDes  import *
import binascii
from Crypto.Cipher import XOR
import string

key='15EA4CA20131C2FD15EA4CA20131C2FD'
key1=binascii.a2b_hex(key)

pin ='041234FFFFFFFFFF'
pan ='0000951360000030'

pin='06111111FFFFFFFF'
pan='0000233300070511'

    
testdata_xor=[(pin,pan)]    
for entry in testdata_xor:
    key,plain=entry
    key=binascii.a2b_hex(key)
    plain=binascii.a2b_hex(plain)
    obj=XOR.new(key)
    ciphertext=obj.encrypt(plain)
    print 'PIN Offset:',string.upper(binascii.b2a_hex(ciphertext))
    data =binascii.b2a_hex(ciphertext)
     


x=triple_des(key1)
e=x.encrypt(binascii.a2b_hex(data))
encdata=binascii.b2a_hex(e)
print 'PIN Block:',string.upper(encdata)

#PIN =1234
#PIN-BLOCK=764B4157966F4B49