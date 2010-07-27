#!/bin/env python

import os
import time
from threading import Thread
import wx
import  wx.lib.newevent
import dlgLogin
from PlurkEngine import PlurkEngine as PE 

try:
    from agw import toasterbox as TB
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.toasterbox as TB

USERNAME=''
PW=''
CHECK_TIMER=120

# new event for the updates
EVT_UNREADCOUNT_UPDATE = wx.NewId()
(UnreadEvent, EVT_UNREADCOUNT_UPDATE) = wx.lib.newevent.NewEvent()

# a flag to break the loop and exit the app
stop_flag = 0

# static login
g_pe = None
def Login():
    global g_pe
    if g_pe == None:
        g_pe = PE()
        try:
            g_pe.Login(USERNAME,PW)
            return g_pe
        except:
            wx.MessageBox("Please restart the program","Login Failed",wx.OK)
    else:
        return g_pe

# to construct the plurk summary list
def GetStatusString(pe,count):
    plurks = pe.GetUnreadPlurks(count)
    users = pe.usersInfo
    summary={}
    for p in plurks:
        # add 1 to the id
        if p['owner_id'] not in summary.keys():
            summary[p['owner_id']] = 1
        else:
            summary[p['owner_id']] += 1

    # build the string
    string = ""
    for k in summary.keys():
        user = users[str(k)]
        string +=  "%s: %d\n" % (user[u'nick_name'], summary[k])
    return string

# show toasterbox
def PlayToasterBox(ui,count,str):
    tb = TB.ToasterBox(ui,TB.TB_SIMPLE, TB.DEFAULT_TB_STYLE, TB.TB_ONTIME)
    tb.SetPopupText(str)
    tb.SetPopupSize((40,40))
    tb.SetPopupPosition((100, 100))
    tb.SetPopupPauseTime(3000)
    tb.SetPopupScrollSpeed(8)
    tb.Play()

# thread func to periodically update the unread count
def UpdateUnreadCount(ui,bloop=1):
    global stop_flag
    ui.SetStatusProcessing(True)

    pe = Login()
    if pe == None:
        ui.Destroy()
        return

    last_count = 0
    str=""
    while True:
        ui.SetStatusProcessing(True)
        count = pe.GetUnreadCount()
        evt=None
        if count == 0:
            print "no new plurks!"
            str="no new plurks!"
            evt = UnreadEvent(_count=0,_str=str)
        else:
            print "you have %s new plurks!" % count
            #evt = UnreadEvent(_count=count,_str="fetching summary..")
            #wx.PostEvent(ui, evt)
            str = GetStatusString(pe,count)
            evt = UnreadEvent(_count=count,_str=str)

        last_count = count

        if evt != None:
            wx.PostEvent(ui, evt)

        # manual update: show messagebox
        if bloop == 0:
            wx.MessageBox(str,"Plurk Updates (%d)" % count ,wx.OK)
            #PlayToasterBox(count,str)

        # not in loop mode, just break the while loop
        if bloop == 0 or stop_flag == 1:
            stop_flag = 0
            break
        time.sleep(CHECK_TIMER)

class PlurkStatusIcon(wx.TaskBarIcon):
    TBMENU_CLOSE   = wx.NewId()
    TBMENU_UPDATE  = wx.NewId()
    
    def __init__(self):
        wx.TaskBarIcon.__init__(self)

        # Set the image
        self.SetIcon(wx.Icon(name="plurk.ico",type=wx.BITMAP_TYPE_ICO), "plurk")
        
        # bind some events
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarUpdate, id=self.TBMENU_UPDATE)

        self.Bind(EVT_UNREADCOUNT_UPDATE, self.OnReadCountUpdate)


    def SetStatusProcessing(self,status):
        if status == True:
            self.SetIcon(wx.Icon(name="processing.ico",type=wx.BITMAP_TYPE_ICO), "plurk")

    def SetApp(self,app):
        self.app = app

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.TBMENU_UPDATE, "Update")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_CLOSE,   "Quit")
        return menu


    def OnTaskBarActivate(self, evt):
        #os.startfile("http://www.plurk.com/plateaukao?mode=unread#")
        os.startfile("http://www.plurk.com/m?mode=unread#")


    # exit the program by destroying the taskbar icon
    def OnTaskBarClose(self, evt):
        stop_flag = 1
        #self.app.t.stop()
        self.Destroy()
        self.app.ExitMainLoop()

    def OnTaskBarUpdate(self, evt):
        UpdateUnreadCount(self,bloop=0)

    def OnReadCountUpdate(self, evt):
        print "OnReadCountUpdate: %d" % evt._count
        if evt._count == 0:
            self.SetIcon(wx.Icon(name="plurk.ico",type=wx.BITMAP_TYPE_ICO), "Plurk")
        elif evt._count < 10:
            f = "unread%s.ico" % evt._count
            self.SetIcon(wx.Icon(name=f,type=wx.BITMAP_TYPE_ICO), "Unread:%d\n%s" % (evt._count,evt._str))
        else:
            self.SetIcon(wx.Icon(name="unreadmore.ico",type=wx.BITMAP_TYPE_ICO), "Unread:%d\n%s" % (evt._count,evt._str))

class MyApp(wx.App):
    def OnInit(self):
        self.login = dlgLogin.create(None)
        self.login.SetApp(self)
        self.login.Show()
        self.tbicon = PlurkStatusIcon()
        self.tbicon.SetApp(self)

        return True

    def OnLogin(self,username, password):
        global USERNAME, PW
        USERNAME = username
        PW = password
        #create thread to update the status
        self.t = Thread(target=UpdateUnreadCount,args=(self.tbicon,))
        self.t.start()
    

def main():
    app = MyApp(False)
    app.MainLoop()

if __name__ == '__main__':
    __name__ = 'Main'
    main()

# vim:set nu et ts=4 sw=4 cino=>4:
