#-*- coding :utf-8 -*-
from enthought.traits.api import *
from enthought.traits.ui.api import *
import time

class Reactor(HasTraits):
    core_temperature = Range(-273.0, 100000.0)
    
class ReactorModelView(ModelView):
    # The "dummy" view of the reactor should be a waring string.
    core_temperature = Property(depends_on='model.core_temperature')
    def _get_core_temperature(self):
        temp = self.model.core_temperature
        if temp <= 500.0:
            return 'Normal'
        if temp < 2000.0:
            return 'Warning'
        return 'Meltdown'
        
my_view = View(Item('core_temperature', style = 'readonly'))

if __name__ == "__main__":
    reactor = Reactor( core_temperature = 200.0 )
    view = ReactorModelView(model=reactor)
    view.edit_traits(view=my_view)
    time.sleep(5.0)
    reactor.core_temperature = 5000.0
    view.edit_traits(view=my_view)
    time.sleep(5.0)
