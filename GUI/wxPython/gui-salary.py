# -*- coding :UTF-8 -*-

import wx,string
class MySalgar(wx.Frame):
    def __init__(self):
        #建造一個新的 Frame
        wx.Frame.__init__(self, parent=None, title=u"薪資試算程式", size=(250,200))
        # 加入一個 Panel
        panel = wx.Panel(self)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MySalgar()
    frame.Show()
    app.MainLoop()
    #基本 Frame -- 結束 --
