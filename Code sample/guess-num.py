#-*- coding:UTF-8 -*-

from random import randint

answer= randint(1,99)
if __name__ =="__main__":
    print "===猜數字"
    print 
    state=True
    while state:
        try:
            guess=int(raw_input("Please enter number: "))
            if guess ==answer:
                print 
                print "You got it!"
                print
                state=False
            elif answer< guess< 100:
                print "Large than answer"
            elif 0< guess < answer:
                print "Small than answer"
            else:
                raise ValueError
        except ValueError:
                print "guess"
    raw_input("Press<Enter> end ")
            