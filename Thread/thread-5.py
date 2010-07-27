import thread
from time import sleep,time,ctime

def loop0():
    print 'start loop0', ctime(time())
    sleep(3)
    print 'loop 0 done', ctime(time())

def loop1():
    print 'start loop1', ctime(time())
    sleep(4)
    print 'loop 1 done', ctime(time())

def main():
    print 'start main'
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(5)
    print 'dll aone', ctime(time())
    
if __name__ ==  '__main__':
    main()
