#-*- coding:utf-8 -*-
from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.menu import *


class Personal(HasTraits):
    first_name=Str()
    last_name=Str()
    year=Int()
    
    def _first_name_changed(self):
        self.last_name=self.first_name
        
        
Personalview1=View(Group(Item('first_name'),
                           Item('last_name'),
                           label='Internal view',
                           show_border=True))
        
Personalview2=View(Group(Item('first_name',style='custom'),
                    Item('last_name',style='text'),
                    orientation='horizontal',layout='split',
                    label='Horizotal View',
                    show_border=True),
                    kind='live',
                    buttons=LiveButtons
                )
    
Personalview3=View(Group(Item('first_name',style='custom'),
                 Item('last_name',style='text'),
                 orientation='vertical',
                 label='Vertical View',
                 show_border=True),                 
                 buttons=ModalButtons
                )
    
ray=Personal()
ray.configure_traits(view=Personalview1)

alex=Personal()
alex.configure_traits(view=Personalview2)

john=Personal()
john.configure_traits(view=Personalview3)
