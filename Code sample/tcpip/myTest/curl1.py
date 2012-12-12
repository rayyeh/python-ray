from datetime import datetime
import os
import random

COUNT = 100
cardlist=[]
pwdlist=[]


for i in range(1,COUNT+1):
    cardbase =[]
    cardno=''
    cardbase.append(str(random.randint(3,5)))
    for x in range(1,16):
        cardbase.append(str(random.randint(0,9)))
    for x in range(0,16):
        cardno=cardno+cardbase[x]
    cardlist.append(cardno)
    
for i in range(1,COUNT+1):
    pwdlist.append(str(random.randint(1000,9999)))

starttime=datetime.now()

for i in range(1,COUNT+1):
    #print str(i)+','+str(cardlist[i-1])+','+str(pwdlist[i-1])
    #cardno='4637817900110000'
    #command="curl http://localhost:8000/TempPWD -F cardnumber="+cardno+' -F password='+pwdlist[i-1]           
    
    
    command="curl http://localhost:8000/TempPWD -F cardnumber="+cardlist[i-1]+' -F password='+pwdlist[i-1]
    os.system(command)

durtime=datetime.now()-starttime

print '*'*60
print '  Tatal execute transaction volume:',COUNT
print '  Totol run time:',durtime
print '  Average per transaction run time:', durtime/COUNT
print '*'*60
