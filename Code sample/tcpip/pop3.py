import poplib
import getpass

mServer = poplib.POP3('pop3.live.com',995)

#Login to mail server
mServer.user('yeh_ray')
mServer.pass_('ych@6316')
stat=mServer.stat()
print mServer.getwelcome( )

#Get the number of mail messages
numMessages = len(mServer.list()[1])

print "You have %d messages." % (numMessages)
print "Message List:"

#List the subject line of each message
for mList in range(numMessages) :
    for msg in mServer.retr(mList+1)[1]:
        if msg.startswith('Subject'):
            print '\t' + msg
            break

mServer.quit()
 
