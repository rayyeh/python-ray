from Tkinter import *
import tkMessageBox

root = Tk()

def helloCallBack():
    tkMessageBox.showinfo("Hello","python")

B = Button(root, text="python", command=helloCallBack)
B.pack()
root.mainloop()

