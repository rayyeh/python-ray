#!/usr/bin/python 
#--- Setup ----------------------------------------------
import urllib, urllib2, cookielib
import simplejson as json

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
api_key = 'G5NekkqlrJN27hix39cTZgmjhDVVWMgy'
get_api_url = lambda x: 'http://www.plurk.com/API%s' % x
get_api_sslurl = lambda x: 'https://www.plurk.com/API%s' % x
encode = urllib.urlencode

#--- Classes ----------------------------------------------
class UserProfile:
    def __init__(self,jO):
        self.friends_count=jO['friends_count']
        self.fans_count=jO['fans_count']
        #self.unread_count=jO['unread_count']
        #self.alers_count=jO['alerts_count']
        self.privacy=jO['privacy']
        self.user_info=jO['user_info']
        self.plurks=jO['plurks']

class PlurkEngine:
    def Login(self,username,password):
        response = opener.open(get_api_sslurl('/Users/login'),
                         encode({'username': username,
                                 'password': password,
                                 'api_key': api_key}))
        
        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print dRes['error_text']
            return false
        
        #parse UserProfile
        self.userProfile = UserProfile(deRes)
        self.usersInfo = self.GetUsersInfo()
        
        self.plurks = self.userProfile.plurks
        #for p in self.plurks:
        #    print p['owner_id'],":",p['content']

    def GetUserProfile(self,id):
        response = opener.open(get_api_url('/Profile/getPublicProfile'),
                         encode({'api_key': api_key,
                                 'user_id': id}))

        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print deRes['error_text']
            return false

        return UserProfile(deRes)

    # use GetCompletion to get all friends nickname info
    def GetUsersInfo(self):
        response = opener.open(get_api_url('/FriendsFans/getCompletion'),
                         encode({'api_key': api_key}))

        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print deRes['error_text']
            return false
        # add self to the user list from userprofile
        s = self.userProfile.user_info
        deRes[str(s['id'])] = {u'nick_name':s['display_name']}
        return deRes

    def GetPlurks(self):
        response = opener.open(get_api_url('/Polling/getPlurks'),
                         encode({'api_key': api_key,
                                 'offset': ''}))

        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print deRes['error_text']
            return false

    def GetUnreadPlurks(self,count):
        response = opener.open(get_api_url('/Timeline/getUnreadPlurks'),
                         encode({'api_key': api_key,
                             'limit':count}))

        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print deRes['error_text']
            return false
        return deRes['plurks']

    def GetUnreadCount(self):
        response = opener.open(get_api_url('/Polling/getUnreadCount'),
                         encode({'api_key': api_key}))

        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print deRes['error_text']
            return false
        return deRes['all']

    def AddPlurk(self,qualifier, text):
        response = opener.open(get_api_url('/Timeline/plurkAdd'),
                         encode({'content': text,
                                 'qualifier': qualifier,
                                 'lang': 'en',
                                 'api_key': api_key}))

        deRes = json.load(response)
        if "error_text" in deRes.keys():
            print deRes['error_text']
            return false
        return deRes

#--- Test ----------------------------------------------------------
if __name__ == '__main__':
    PASSWORD = ""
    USERNAME = ""

    # test login
    pe = PlurkEngine()
    pe.Login(USERNAME,PASSWORD)
    print pe.GetUnreadCount()

    plurks = pe.GetUnreadPlurks(50)
    #plurks = pe.plurks
    # test usersInfo
    for user in pe.usersInfo:
        print user,pe.usersInfo[user][u'nick_name']

    # test nick_name and plurk content
    for p in plurks:
        print p
        print pe.usersInfo[str(p['owner_id'])][u'nick_name'],":",p['content']

    # test add plurk
    #pe.AddPlurk('says','hello world from python')


# vim:set nu et ts=4 sw=4 cino=>4:
