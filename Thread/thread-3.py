import threading
import time

class printTime ( threading.Thread ) :
        def __init__( self, delay ):
                threading.Thread.__init__( self )
                self.delay = delay
        def run( self ):
                while 1:
                        time.sleep( self.delay )
                        try:
                        	print gtime
                        except:
                        	pass

class timeHandle:
        def __init__ ( self, delay ):
                self.delay = delay
        def globalTime(self):
                global gtime
                while 1:
                        time.sleep( self.delay )
                        gtime = time.ctime ( time.time() )

if __name__ == "__main__":
	pt = printTime( 5 )
	pt.start()
	th = timeHandle( 5 )
	th.globalTime()
