#!/usr/bin/python
"""
    examples.py
    Copyright 2008 David Blume <david.blume@gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

import plurkapi
import sys

#
# Create an API object.
# Pass in your own username and password to the "login" method.
#
plurk_api = plurkapi.PlurkAPI()
if plurk_api.login('yehrayyeh', 'ych@6316') == False:
    print "Login failed!"
    sys.exit(1)
    
#
# Disply your karma.
#
user_info = plurk_api.uidToUserinfo(plurk_api.uid)
print "%s has %1.1f karma." % (plurk_api.nickname, user_info['karma'])

#
# Display each friend's uid.
#
for key in plurk_api.friends:
    print "  %s's uid is %s." % (plurk_api.friends[key]['nick_name'], key)

#
# Display a list of plurks.
#
plurks = plurk_api.getPlurks()
print "Plurk at %s: %s %s %s" % (plurks[0]['posted'],
                                 plurk_api.uidToNickname(plurks[0]['owner_id']),
                                 plurks[0]['qualifier'],
                                 plurks[0]['content'])
#
# Get and accept all friend requests
# 
alerts = plurk_api.getAlerts()
if len(alerts):
    plurk_api.befriend(alerts)

#
# Add a plurk
#
#    plurk_api.addPlurk(qualifier='says', content='Hello world!')

#
# Respond to a plurk
#
#    if plurks[0]['no_comments'] == 0:
#        plurk_api.respondToPlurk(plurks[0]['plurk_id'], qualifier='says', content='This is my first response')


