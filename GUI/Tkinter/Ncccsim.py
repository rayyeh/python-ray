#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter


class ncccsim(Tkinter.Tk):

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self, text=u"Connect Server ",
                 command=self.OnConnectClick, relief=Tkinter.RAISED)
        button.grid(column=0, row=0, sticky='W')
        self.entryIP = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryIP, width=20)
        self.entry.grid(column=1, row=0)
        'self.entry.bind("<Return>", self.OnPressEnter)'
        self.entryIP.set(u"Enter Server IP")

        button = Tkinter.Button(self, text=u"Send NCCC Message",
                                command=self.OnSendClick)
        button.grid(column=0, row=1, sticky='W')
        self.messageIn = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.messageIn)
        self.entry.grid(column=1, row=1, sticky='W')
        'self.entry.bind("<Return>", self.OnPressEnter)'

        self.messageOut = Tkinter.StringVar()
        label = Tkinter.Message(self, textvariable=self.messageOut,
                                anchor="w", fg="white")
        label.grid(column=0, row=2, sticky='EW')
        self.messageOut.set(u"Display Message!")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnConnectClick(self):
        self.messageOut.set(self.entryIP.get())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnSendClick(self):
        self.messageOut.set(self.messageIn.get())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event):
        self.labelVariable.set(
            self.entryVariable.get() + " (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = ncccsim(None)
    app.title('NCCC Simulator')
    app.mainloop()
