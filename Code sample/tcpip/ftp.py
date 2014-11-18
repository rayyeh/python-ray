print '#' * 50
print '#Demo:Using Python to Fetch Files from an FTP Server'
print '#' * 50

import os, sys
from getpass import getpass

nonpassive = False  # force active mode FTP for server?
filename = 'perso_out.log'  # file to be downloaded
dirname = '.'  # remote directory to fetch from
sitename = '192.168.110.134'  # FTP site to contact
# userinfo    = ('dev_svct', getpass('vfr43edc'))      # use ( ) for anonymous
if len(sys.argv) > 1: filename = sys.argv[1]  # filename on command line?

print 'Connecting...'
from  ftplib import FTP  # socket-based FTP tools

localfile = open(filename, 'wb')  # local file to store download
connection = FTP(sitename)  # connect to FTP site
connection.login('dev_svct', 'vfr43edc')  # default is anonymous login
connection.cwd(dirname)  # xfer 1k at a time to localfile
if nonpassive:  # force active FTP if server requires
    connection.set_pasv(False)

print 'Downloading...'
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

# if raw_input('Open file?') in 'Yy':
#    from PP3E.System.Media.playfile import playfile
#    playfile(filename)
