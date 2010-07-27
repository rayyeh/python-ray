from wapich  import *   #import python wrap data
from ctypes import *

libc=cdll.LoadLibrary('wapicd.dll')
WS_Initialize=libc.WS_Initialize  #define  function
WS_Initialize.restype=WS_RV    # set return type  = WS_RV, if none, always return int 

rv=WSR_OK
rv=WS_Initialize() 

if rv != WSR_OK:
   print rv
else:
    print 'WS_Initialize is Ok'

WS_GetInfo=libc.WS_GetInfo
WS_GetInfo.restype=WS_RV

myInfo=WS_INFO()  
myInfo_p=pointer(myInfo)
myInfo_p.contents=myInfo   # assign 

rv=WSR_OK
rv=WS_GetInfo(myInfo_p)
if rv !=WSR_OK:
    print rv

print 'myInfo .manufacturerID:',  myInfo.manufacturerID[:]
print 'myInfo.description:', myInfo.description[:]
print 'myInfo.version.major:', myInfo.version.major
print 'myInfo.version.minor:', myInfo.version.minor
