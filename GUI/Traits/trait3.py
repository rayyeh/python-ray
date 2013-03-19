#-*- coding:utf-8 -*-


from enthought.traits.api import HasTraits,String
from enthought.traits.ui.api import View,Item

class Trait3(HasTraits):
    input=String()
    output =String()
    
    def _input_changed(self):
        self.output=self.input
    
    view=View(Item('input',label="Input"),
              Item('output',label="Output")
              )

if __name__ =="__main__":
    t1=Trait3()
    t1.configure_traits()