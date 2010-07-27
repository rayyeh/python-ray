#-*- coding: UTF-8 -*-

"""
   這是測試程式
"""

if __name__ == "__main__":
    try:
        f=open(raw_input("請輸入檔名:"),"r")
        print "*"*50
        print f.read()
        print "*"*50
        f.close()
    except IOError:
        print "no such file!"

    print
    raw_input("請按<Enter>結束")



