#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
from socket import *
import binascii


class ncccsim(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        button1 = Button(self, text=u"Server IP",
                         command=self.OnConnectClick, relief=FLAT)
        button1.grid(column=0, row=0, sticky="E" + "W")
        self.entryIP = StringVar()
        self.entry = Entry(self, textvariable=self.entryIP, width=20)
        self.entry.grid(column=1, row=0, sticky="E" + "W")
        'self.entry.bind("<Return>", self.OnPressEnter)'
        self.entryIP.set(u"192.168.110.91")

        label = Label(self, text=u"Port ")
        label.grid(column=2, row=0, sticky="E" + "W")
        self.entryPort = IntVar()
        self.entry = Entry(self, textvariable=self.entryPort, width=4)
        self.entry.grid(column=3, row=0, sticky="E" + "W")
        'self.entry.bind("<Return>", self.OnPressEnter)'
        self.entryPort.set(u"1658")

        button2 = Button(self, text=u"NCCC Message",
                         command=self.OnSendClick)
        button2.grid(column=0, row=1, sticky="E" + "W")
        self.messageIn = StringVar()
        self.entry = Entry(self, textvariable=self.messageIn, bg="white")
        self.entry.grid(column=1, row=1, columnspan=3, sticky="E" + "W")
        'self.entry.bind("<Return>", self.OnPressEnter)'

        button2 = Button(self, text=u"Quit", command=self.OnQuitClick)
        button2.grid(column=3, row=1, sticky="E" + "W")

        self.messageOut = StringVar()
        text = Message(self, textvariable=self.messageOut,
                       justify=LEFT, bg="white")
        text.grid(column=0, row=3, sticky='N' + "E" + "W" + "S", columnspan=4)
        self.messageOut.set(u"Display Message!")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)
        self.update()
        self.geometry(self.geometry())

    def OnConnectClick(self):
        ServerIP = self.entryIP.get()
        ServerPort = self.entryPort.get()
        print 'conneting %s,%s' % (ServerIP, ServerPort)
        sSock = socket(AF_INET, SOCK_STREAM)
        sSock.connect((ServerIP, ServerPort))
        self.messageOut.set(u'conneting %s,%s' % (ServerIP, ServerPort))
        self.entry.focus_set()
        self.entry.selection_range(0, END)

    def OnSendClick(self):
        ServerIP = self.entryIP.get()
        ServerPort = self.entryPort.get()
        print 'conneting %s,%s' % (ServerIP, ServerPort)
        sSock = socket(AF_INET, SOCK_STREAM)
        sSock.connect((ServerIP, ServerPort))
        x = hex(len(self.messageIn.get()))
        x.split('x')
        b = x[2:]
        header = '0000'
        header = header[:4 - len(b)] + b
        msg = binascii.a2b_hex(header) + self.messageIn.get()
        sSock.send(msg)
        data = sSock.recv(1024)
        self.messageOut.set(data)
        'self.messageOut.focus_set()'
        'self.messageOut.selection_range(0, END)'

    def OnQuitClick(self):
        self.destroy()

    def OnPressEnter(self, event):
        self.labelVariable.set(
            self.entryVariable.get() + " (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, END)


if __name__ == "__main__":
    app = ncccsim(None)
    app.title('NCCC Simulator')
    app.mainloop()
