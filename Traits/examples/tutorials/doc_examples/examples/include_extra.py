#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

# include_extra.py --- Example of Include object
#                      provided for subclasses
from enthought.traits.api import HasTraits, Int, Str, Trait
from enthought.traits.ui.api import Group, Include, View
import enthought.traits.ui

class Person(HasTraits):
    name = Str
    age = Int
    
    person_view = View('name', Include('extra'), 'age',
                       kind='livemodal')
    
Person().configure_traits()

class LocatedPerson(Person):
    street = Str
    city = Str
    state = Str
    zip = Str
    
    extra = Group('street', 'city', 'state', 'zip')
    
LocatedPerson().configure_traits()

