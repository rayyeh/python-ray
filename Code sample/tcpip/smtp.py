# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import sys,time
debuglevel = 0

s = smtplib.SMTP()
s.set_debuglevel(debuglevel)

s.connect("192.168.10.6",25) #default port 25
#s.login('rayyeh@uitc.com.tw','JUN06jun')
from_addr= "rayyeh@uitc.com.tw"
to_addr = "rayyeh@uitc.com.tw"
Subject = "Mail from python"
Text = "do you see  the context"
Date = time.ctime(time.time())

s.ehlo()
#s.starttls()
s.ehlo()
#Format mail message
mMessage = ('From: %s\nTo: %s\nDate: \
            %s\nSubject: %s\n%s\n' %
            (from_addr,to_addr,Date,Subject,MIMEText(Text)))
print mMessage


s.helo('smtp.uitc.com.tw')
s.sendmail(from_addr,to_addr,mMessage)
s.close()
