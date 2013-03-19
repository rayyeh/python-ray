from enthought.traits.api import HasTraits,Property,Float \
            ,cached_property,Any,on_trait_change 
from enthought.traits.ui.api import Item,View,HGroup,VGroup

class trait1(HasTraits):
    widght = Float(2.0)
    height =Float(3.0)
    area = Property(depends_on=['widght','height'])
    value = Property
    _the_shadow = Any
    value =Float(1.0)
    
    
    #view=View('widght','height',Item('area',style='readonly'))
    view=View(
              VGroup(# Create a Vertical layout group
                     HGroup(# And a Horizontal group within that
                            # Change the labels on each item.
                            Item('widght',label='w'),
                            Item('height',label='h'),
                            Item('value',label='x value')
                            ),
                            Item('area',style='readonly'),
                    ),
                    buttons=['Ok','Cancel']
            )
    
    def _get_area(self):
        print 'recalculating'
        return self.widght*self.height
    
    def _get_value(self):
        print 'Get x'
        return self._the_shadow
    
    def _set_value(self,value):
        print 'Set x'
        self._the_shadow = value        
    
    #Valid Static Trait Notification Signatures
    def _value_changed(self,old,new):        
        print 'Before value:',old
        print 'After value:',new
        print 'Changed data  :',self.value
        
    @on_trait_change('value,height')
    def update(self,name,value):
        print 'trait %s changed to %s',(name,value)
    
if __name__ == "__main__":
    rec =trait1(widght=2.0,height=3.0)
    #rec.on_trait_change(printer,name='value')
    rec.value = 11
    rec.configure_traits()
    