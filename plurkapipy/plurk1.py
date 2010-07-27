#!/usr/bin/python
# -*- coding: UTF-8 -*-

import plurkapi
import sys

# Create an API object.
# Pass in your own username and password to the "login" method.
#

plurk_api = plurkapi.PlurkAPI()

#if plurk_api.login('yehrayyeh', 'ych@6316') == False:
#   print "Login failed!"
#  sys.exit(1)

# print my plurk id
print  'my uid: ', plurk_api.uid
myUID = plurk_api.uid
print  myUID

#Plurk a message to Plurk
#plurk_api.addPlurk(lang='tr_ch',qualifier='says',content='Using Python and plurkapi')

#Print friends Nickname and  UID
print 'Friends:', plurk_api.friends
for friend in plurk_api.friends:    
    print 'Nick_name:', plurk_api.friends[friend][u'nick_name'] , \
            ' Full_name:', plurk_api.friends[friend][u'full_name'], \
            ' Uid:', friend
  
print ' ======================'
print '===   Get yours friends plurks  =='
#Get  Plurk messages
#plurks = plurk_api.getPlurks()
#for i in  range(2):
#   print "Plurk at %s: %s %s %s  %s" % (plurks[i]['posted'],
#                                plurk_api.uidToNickname(plurks[i]['owner_id']),
#                                plurks[i]['qualifier'],
#                                plurks[i]['content'], 
#                                plurks[i]['plurk_id'])

print '===  print plurk by uid ========'
plurks = plurk_api.getPlurks(uid=3892259,date_from = 2008-9-5)
for plurk in plurks :
    print "Plurk at %s: %s %s %s  %s" % (plurk['posted'],
                                plurk_api.uidToNickname(plurk['owner_id']),
                                plurk['qualifier'],
                                plurk['content'], 
                                plurk['plurk_id'])
