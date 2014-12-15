from __future__ import division
from builtins import str
from builtins import range
from past.utils import old_div
from datetime import datetime
import os
import random

COUNT = 1
DEBUG = True
CARDNO = '4637817900110000'
PWD = '1234'
cardlist = []
pwdlist = []

print 'The job will run %s times' % COUNT

if DEBUG == False:
    for i in range(1, COUNT + 1):
        cardbase = []
        cardno = ''
        cardbase.append(str(random.randint(3, 5)))
        for x in range(1, 16):
            cardbase.append(str(random.randint(0, 9)))
        for x in range(0, 16):
            cardno = cardno + cardbase[x]
        cardlist.append(cardno)
    for i in range(1, COUNT + 1):
        pwdlist.append(str(random.randint(1000, 9999)))

starttime = datetime.now()

for i in range(1, COUNT + 1):
    if DEBUG == False:
        print str(i) + ',' + str(cardlist[i - 1]) + ',' + str(pwdlist[i - 1])
        command = "curl http://localhost:8000/TempPWD -F cardnumber=" + cardlist[i - 1] + ' -F password=' + pwdlist[
            i - 1]
    else:
        command = "curl http://localhost:8000/TempPWD -F cardnumber=" + CARDNO + ' -F password=' + PWD

    os.system(command)

durtime = datetime.now() - starttime

print '*' * 60
print '  Tatal execute transaction volume:', COUNT
print '  Totol run time:', durtime
print '  Average per transaction run time:', old_div(durtime, COUNT)
print '*' * 60
