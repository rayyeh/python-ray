''' Using telnetlib to simulate CAT CRIN transaction '''
import getpass
import sys
import telnetlib
import time
import binascii
from time import strftime


HOST = "192.168.110.91"
user = "UITC.APYCH"
password = "2222222 "

tn = telnetlib.Telnet("192.168.110.93")
print "HOST"
tn.set_debuglevel(9)
time.sleep(1)

tn.read_until("Enter Choice> ")
time.sleep(2)
tn.write("CATUCOS"+"\r\n")
Req_Msg=''
Rsp_Msg=''

def LOGI():
    x=strftime("%H%M%S%y%m%d")
    sendtime=x[6:]+x[0:6]
    #print('SendTime:', sendtime)
    #print('Time:',x)
    y=[]
    for i in range(6):
        j=i*2+1
        #print(i)
        k=int(x[j])+1
        y.append(k)
    #print('hmsYMD:',y)
    z=[]
    z.append(int(y[2])*3)
    z.append(int(y[5])*5)
    z.append(int(y[1])*4)
    z.append(int(y[2])*6)
    z.append(int(y[4])*5)
    z.append(int(y[0])*2)
    z.append(int(y[3])*3)
    z.append(int(y[2])*7)
    #print(z)
    EncPwd=[]
    PWD=''
    for i in range(8):
        #print(password[i])
        #print('pwd ele:',ord(password[i]))
        EncPwd.append(ord(password[i])+z[i])
        if EncPwd[i] > 127:
            EncPwd[i] = EncPwd[i] - 96
    #print(EncPwd)
    PWD=''.join(chr(e) for e in EncPwd)
    #print('PWD:',PWD)


    '''data ='1C48   4541   4445   524C    4F47   4930   3030   3030    3030   3054   5220   3030 \
    3030   3030   3030   3030    2041   4646   4646   4646    1C4C   4F47   4930   3053 \
    5550   4552   2020   2035    645A   383C   3444   2730    3030   3120   2020   2020 \
    2020   2020   2020   2020    2020   2031   3530   3132    3931   3634   3934   3031 \
    2E32   2055   424F   5420    2020   2020   2020   2020    2020   200D' '''

    msg0 = 'HEADERLOGI00000000TR 0000000000 AFFFFFF'
    msg1= ' 1C4C   4F47   4930   3053 5550   4552   2020   20'
    msg2 ='30    3030   3120   2020   2020 2020   2020   2020   2020    2020   20'
    msg3 ='312E32   2055   424F   5420    2020   2020   2020   2020    2020   200D'



    data1 =msg1.split(' ')
    data2=''.join(data1)
    data3=msg2.split(' ')
    data4=''.join(data3)
    data5=msg3.split(' ')
    data6=''.join(data5)

    str1=binascii.a2b_hex(data2)
    str2=binascii.a2b_hex(data4)
    str3=binascii.a2b_hex(data6)
    LOGIMSG ='\x1c'+msg0+str1+PWD+str2+sendtime+str3
    return LOGIMSG

def CRIN_READ():
    msg0 = "\x1c"+'HEADERCRIN99999999ER 0000000000 BFFFFFF'
    msg1 = "\x1c"+"CRIN004579523300000209   "+strftime("%H%M%S%S")+" "*26+"\x0d\x00"
    CRIN_READ_MSG=msg0+msg1
    return CRIN_READ_MSG

def CRIN_UPDATE(x):
    header=[]
    header = list(x[1])
    header[19] ="U"
    msg0 = "\x1c"+ "".join(header)
    msg1 = "\x1c"+"CRIN004579523300000209   "+strftime("%H%M%S")+"00"+" "*26

    CBF_Limit = "+0000889999900"
    CBF_Expiry = "20150204"
    GLF_Limit = "+0000889999900"
    GLF_Expiry = "20150204"
    msg2 = "\x1c"+x[3][0:102]+CBF_Limit+CBF_Expiry+x[3][124:194]+GLF_Limit+GLF_Expiry+"Approved"+" "*32+"\x0D"
    msg3=msg0+msg1+msg2

    CRIN_UPDATE_MSG = msg3

    return CRIN_UPDATE_MSG

#  LOGI to COSES
tn.write(LOGI())
tn.read_until('\x03')

#CRIN Read
Req_Msg =CRIN_READ()
tn.write(Req_Msg)
Rsp_Msg=tn.read_until("\x03")

x=Rsp_Msg.split('\x1c')
Req_Msg =CRIN_UPDATE(x)
tn.write(Req_Msg)
Rsp_Msg=tn.read_until("\x03")
print(Rsp_Msg)

