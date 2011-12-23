# Program name = ntp.py
# This program is for Nonstop server NTP client
# prerequirements : HP Nonstop OSS , Pyhton 2.4.2 (get it from ITUGLIB,http://ituglib.connect-community.org), and 
# donwload ntplib-0.1.9 from Python Package Index
# You have to modify ntplib.py in ntplib-0.1.9 to accept ip address NTP. Here is snippet
#   def request(self, host, version=2, port='ntp'):
#       """make a NTP request to a server - return a NTPStats object"""
#        # lookup server address
#        #addrinfo = socket.getaddrinfo(host, port)[0]
#        #family, sockaddr = addrinfo[0], addrinfo[4]
#        family=2
#        sockaddr=(host,123)

# You need to use Super Group to run the program.Because SETTIME is Super Group ONLY.
# Usage : gtacl -c "$(python ntp.py)"


import ntplib
import os
from time import ctime
c = ntplib.NTPClient()
response = c.request('172.30.1.119', version=3)
response.offset
response.version
ntptime=ctime(response.tx_time)
ntptimelist =ntptime.split()
newtime=ntptimelist[1]+' '+ntptimelist[2]+' '+ntptimelist[4]+','+ntptimelist[3]

#print ntplib.leap_to_text(response.leap)
#print response.root_delay

settimestring = "settime"+' '+newtime
print settimestring
#print "time"	


#os.system('gtacl -c "time"')
#os.system('gtacl -c "status *"')
#os.system('gtacl -p fup "info \uitc.\$dev.cup.*"')