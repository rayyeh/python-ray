#Boa:Dialog:DlgLogin

import wx
import ConfigParser

def create(parent):
    return DlgLogin(parent)

[wxID_DLGLOGIN, wxID_DLGLOGINBTNLOGIN, wxID_DLGLOGINSTATICTEXT1, 
 wxID_DLGLOGINSTATICTEXT2, wxID_DLGLOGINTEXTCTRL1, wxID_DLGLOGINTEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class DlgLogin(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DLGLOGIN, name='DlgLogin', parent=prnt,
              pos=wx.Point(423, 322), size=wx.Size(254, 205),
              style=wx.DEFAULT_DIALOG_STYLE, title='Plurk Login')
        self.SetClientSize(wx.Size(246, 178))

        self.staticText1 = wx.StaticText(id=wxID_DLGLOGINSTATICTEXT1,
              label='Username:', name='staticText1', parent=self,
              pos=wx.Point(24, 32), size=wx.Size(58, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DLGLOGINSTATICTEXT2,
              label='Password:', name='staticText2', parent=self,
              pos=wx.Point(24, 64), size=wx.Size(55, 14), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DLGLOGINTEXTCTRL1,
              name='textUsername', parent=self, pos=wx.Point(104, 32),
              size=wx.Size(100, 22), style=0, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DLGLOGINTEXTCTRL2,
              name='textPassword', parent=self, pos=wx.Point(104, 64),
              size=wx.Size(100, 22), style=wx.TE_PASSWORD, value='')

        self.btnLogin = wx.Button(id=wxID_DLGLOGINBTNLOGIN, label='Login',
              name='btnLogin', parent=self, pos=wx.Point(40, 104),
              size=wx.Size(152, 48), style=0)
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnBtnLoginButton,
              id=wxID_DLGLOGINBTNLOGIN)

    def __init__(self, parent):
        self._init_ctrls(parent)
	self.cfg = ConfigParser.ConfigParser()
	try:
            self.cfg.read("plurkmonitor.ini")
            self.username = self.cfg.get("account","username","")
            self.password = self.cfg.get("account","password","")
	    self.textCtrl1.SetValue(self.username)
	    self.textCtrl2.SetValue(self.password)
        except:
            pass		

    def SetApp(self,a):
        self.app = a
    def OnBtnLoginButton(self, event):
        self.cfg.set("account", "username",self.textCtrl1.GetValue())
        self.cfg.set("account", "password",self.textCtrl2.GetValue())
	self.cfg.write(open("plurkmonitor.ini",'w'))

        self.app.OnLogin(self.textCtrl1.GetValue(), self.textCtrl2.GetValue())
        self.Destroy()
