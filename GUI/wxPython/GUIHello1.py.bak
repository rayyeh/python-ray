# -*- coding: UTF-8 -*-

import wx
from time import asctime

weeks = {"Mon": u"星期一", "Tue": u"星期二", "Wed": u"星期三", \
         "Thu": u"星期四", "Fri": u"星期五", "Sat": u"星期六", \
         "Sun": u"星期日"}
months = {"Jan": u"一月", "Feb": u"二月", "Mar": u"三月", \
          "Apr": u"四月", "May": u"五月", "Jun": u"六月", \
          "Jul": u"七月", "Aug": u"八月", "Sep": u"九月", \
          "Oct": u"十月", "Nov": u"十一月", "Dec": u"十二月"}


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, \
                          size=(400, 300))
        panel = wx.Panel(self, -1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        prompt = u"請輸入你的名字"
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, -1, prompt)
        st1.SetFont(font)
        hbox1.Add(st1, 0, wx.RIGHT, 14)
        self.name = wx.TextCtrl(panel, -1)
        hbox1.Add(self.name, 1)

        vbox.Add(hbox1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT \
                 | wx.TOP, 12)
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.button = wx.Button(panel, 1, "Say Hello....")
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, id=1)
        hbox2.Add(self.button, 0)

        vbox.Add(hbox2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, \
                 12)
        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.message = wx.StaticText(panel, -1)
        self.message.SetFont(font)
        hbox3.Add(self.message, 0, wx.Right, 14)

        vbox.Add(hbox3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, \
                 12)
        vbox.Add((-1, 10))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.time1 = wx.StaticText(panel, -1)
        self.time1.SetFont(font)
        hbox4.Add(self.time1, 0, wx.Right, 16)

        vbox.Add(hbox4, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, \
                 12)
        vbox.Add((-1, 12))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.time2 = wx.StaticText(panel, -1)
        self.time2.SetFont(font)
        hbox5.Add(self.time2, 0, wx.Right, 16)

        vbox.Add(hbox5, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, \
                 12)
        vbox.Add((-1, 12))

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        self.time3 = wx.StaticText(panel, -1)
        self.time3.SetFont(font)
        hbox6.Add(self.time3, 0, wx.Right, 16)

        vbox.Add(hbox6, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, \
                 12)
        vbox.Add((-1, 12))

        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def ButtonClick(self, event):
        name = self.name.GetValue()
        message = u"哈囉， " + unicode(name) + u" ！"
        self.message.SetLabel(message)

        moment = asctime()
        s1 = u"今天是西元" + unicode(moment[20:]) + u"年"
        s2 = months[moment[4:7]] + \
             unicode(moment[8:10]) + \
             u"日" + weeks[moment[:3]]
        s3 = u"現在時間是" + unicode(moment[11:19])
        self.time1.SetLabel(s1)
        self.time2.SetLabel(s2)
        self.time3.SetLabel(s3)


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, -1, title="Hello Test!!")
    app.MainLoop()
