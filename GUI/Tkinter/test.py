from future import standard_library
standard_library.install_aliases()
import tkinter
import tkinter.messagebox

root = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox.showinfo("Hello","python")

B = tkinter.Button(root, text="python", command=helloCallBack)
B.pack()
root.mainloop()

