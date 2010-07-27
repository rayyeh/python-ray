#-*- coding:UTF-8 -*-

from getpass import getpass

data ={"kaiching":"0000","ray":"1234"}

def hello(name):
    print
    print "Welcome",name,"!"

if __name__ =="__main__":
    name = raw_input("input your name: ")
    word = getpass("Enter password")   
    if data.has_key(nane):
        if word==data[name]:
            hello(name)
        else:
            print "password wrong!"
    else:
        print "please register"

    print raw_input("press<Enter>")
