# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import sys, time

debuglevel = 0

s = smtplib.SMTP()
s.set_debuglevel(debuglevel)

s.connect("172.28.233.14", 25)  # default port 25
# s.login('rayyeh@uitc.com.tw','JUN06jun')
from_addr = "rayyeh@uitc.com.tw"
to_addr = "rayyeh@uitc.com.tw"
Subject = "Mail from python"
Date = time.ctime(time.time())
Text = Date

s.ehlo()
# s.starttls()
s.ehlo()
#Format mail message
mMessage = ('From: %s\nTo: %s\nDate: \
            %s\nSubject: %s\n%s\n' %
            (from_addr, to_addr, Date, Subject, MIMEText(Text)))
#print mMessage

s.helo('smtp.uitc.com.tw')
s.sendmail(from_addr, to_addr, mMessage)
s.close()
