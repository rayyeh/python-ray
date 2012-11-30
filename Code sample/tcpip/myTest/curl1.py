from datetime import datetime
import os
import random

count = 100
starttime=datetime.now()
for i in range(count+1):
	cardnumber = random.randint(1000000000000000,59999999999999999)
	password=random.randint(1000,9999)
	command="curl http://localhost:8000/TempPWD -F cardnumber="+str(cardnumber)+' -F password='+str(password)
	os.system(command)
	
durtime=datetime.now()-starttime

print '*'*60
print '  Tatal execute transaction volume:',count
print '  Totol run time:',durtime
print '  Average per transaction run time:', durtime/count
print '*'*60
