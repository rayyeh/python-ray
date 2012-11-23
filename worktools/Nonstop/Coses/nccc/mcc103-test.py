#######################################################
## Demo:Opening a Server-Side Socket for Receiving Data
#######################################################
print '#'*60
print '# Demo:Opening a Server-Side Socket for Receiving Data'
print '#'*60

from socket import *
import binascii

serverHost = '' # listen on all interfaces
serverPort = 1658

Resp1='ISO0860000580310C22000000201801000000020080001401651795146000017090116093557'
Resp2='00076000BK1631000000000000000000000000000000000000000000000000000000000000000000090105890160000PRO200000000000000YY000000000000000000000000000000502MC059PATHMCC5MCC103         000005433812300392507               026E090110090111C090109090206'
traceNum='123456'

  
x=hex(len(Resp1+traceNum+Resp2))
print x.split('x')
b=x[2:]
print b
header='0000'
header=header[:4-len(b)]+b
print 'xxxx:',header
txt=binascii.a2b_hex(header)+Resp1+traceNum+Resp2
print txt
   
