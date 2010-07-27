from calendar import month
from enthought.traits.api import HasTraits,Property,Float \
            ,cached_property,Any,on_trait_change,Range,Str
from enthought.traits.ui.api import View
class InteractiveMonth(HasTraits):
    month =Range(1,12,1)
    year =Range(-1000,3000,value =2005)
    calendar=Str(label='')
    
    def _anytraits_changed(self):
        self.calendar=month(self.year,self.month)
    
    view=View('month*','year*','calendar~',
              width=310,height=280)


if __name__ == "__main__":
    m=InteractiveMonth()   
    m.configure_traits()