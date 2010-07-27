import smtplib, sys,time
From = "rayyeh@hotmail.com"
To = ["test"]
Date = time.ctime(time.time())
Subject = "New message from Brad Dayley."
Text = "Message Text"
#Format mail message
mMessage = ('From: %s\nTo: %s\nDate: \
            %s\nSubject: %s\n%s\n' %
            (From, To, Date, Subject, Text))

s = smtplib.SMTP()
s.set_debuglevel(1)
s.connect('smtp.uitc.com.tw') #default port 25
s.ehlo()
s.starttls()
s.ehlo()
s.helo('smtp.uitc.com.tw')
s.login('rayyeh@uitc.com.tw','MAR03mar')
s.sendmail('yeh_ray@hotmail.com', 'rayyeh@uitc.com.tw', mMessage)
s.close()
