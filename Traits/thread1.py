from threading import *
from time import sleep
from enthought.traits.api import *
from enthought.traits.ui.api import *


class TextDisplay(HasTraits):
     show=Str()
     view=View(Item('show',show_label=False, springy=True, style='custom'))

class MyThread(Thread):
    display=Instance(TextDisplay)
    view=View(Item('display',show_label=False,style="custom"))
    print 'MyThread starting'
    
    def run(self):
        sleep(5)
        self.display.string ='Hi'    
        
        
my_thread=MyThread()
my_thread.start()
print 'Main Thread  done'