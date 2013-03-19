#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

""" 
A simple demonstration of how to use the ImageEditor to add a graphic element
to a Traits UI View.
"""

# Imports:
import enthought.traits.ui

from os.path \
    import join, dirname
    
from enthought.traits.api \
    import HasTraits, Str
    
from enthought.traits.ui.api \
    import View, VGroup, Item
    
from enthought.traits.ui.api \
    import ImageEditor

from enthought.pyface.image_resource \
    import ImageResource
    
# Constants:

# Necessary because of the dynamic way in which the demos are loaded:
search_path = [ join( dirname( enthought.traits.api.__file__ ),
                      '..', '..', 'examples', 'demo', 'Extras' ) ]

# Define the demo class:    
class Employee ( HasTraits ):
    
    # Define the traits:
    name  = Str
    dept  = Str
    email = Str
  
    # Define the view:
    view = View(
        VGroup(
            VGroup(
                Item( 'name',
                      show_label = False,
                      editor = ImageEditor( 
                          image = ImageResource( 'info',
                                                 search_path = search_path) ) )
            ),
            VGroup( 
                Item( 'name' ),
                Item( 'dept' ),
                Item( 'email' )
            )
        )
    )
    
# Create the demo:    
popup = Employee( name  = 'William Murchison', 
                  dept  = 'Receiving',
                  email = 'wmurchison@acme.com' )
        
# Run the demo (if invoked form the command line):                 
if __name__ == '__main__':
    popup.configure_traits()    

