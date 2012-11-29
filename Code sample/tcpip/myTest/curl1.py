from datetime import datetime
import os
count = 200
starttime=datetime.now()
for i in range(count+1):
	os.system("curl http://localhost:8000/TempPWD -F cardnumber=123456789  -F password=hello")
	
durtime=datetime.now()-starttime

print '*'*60
print '  Tatal execute transaction volume:',count
print '  Totol run time:',durtime
print '  Average per transaction run time:', durtime/count
print '*'*60
