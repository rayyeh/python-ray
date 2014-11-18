# -*- coding :UTF-8 -*-

import wx, string


class MySalgar(wx.Frame):
    def __init__(self):
        # �سy�@�ӷs�� Frame
        wx.Frame.__init__(self, parent=None, title=u"�~��պ�{��", size=(250, 200))
        # �[�J�@�� Panel
        panel = wx.Panel(self)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MySalgar()
    frame.Show()
    app.MainLoop()
    # �� Frame -- ���� --
