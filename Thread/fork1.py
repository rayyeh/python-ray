import os, time

def counter(count):
    for i in range(count):
        print ' I am child [%s]' %(os.getpid( ))
        time.sleep(1)
        print '[%s] => %s' % (os.getpid( ), i)

for i in range(10):
    pid = os.fork( )
    if pid != 0:
        print 'Process %d spawned' % pid
    else:
        counter(10)
        os._exit(0)

print 'Main process exiting.'