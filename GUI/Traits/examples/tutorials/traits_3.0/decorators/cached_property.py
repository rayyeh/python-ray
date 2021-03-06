# Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

#--(cached_property Decorator)--------------------------------------------------
"""
cached_property Decorator
=========================

New in Traits 3.0 is the *cached_property* method decorator which helps
streamline the process of writing properties which cache their current value.

Defining properties is a very powerful technique for exposing as traits items
whose value depends upon the current state of other object traits. In 
particular, this can be very useful for creating synthetic traits which are 
editable or displayable in a traits-based user interface.

In some cases however, the cost of computing the current value of a property
may be fairly expensive, so it is often a good idea to *cache* the most recently
computed value of the property, and return it as the value of the property until
one of the traits the property depends upon changes value, at which point the
cache should be cleared and the property value recomputed the next time its
value is requested.

Combined with the **Property** *depends_on* metadata, the *cached_property*
decorator greatly simplifies the process of writing a cached property. Take a
look at the following code for example::
    
    class TestScores ( HasPrivateTraits ):
        
        scores  = List( Int )
        average = Property( depends_on = 'scores' )
        
        @cached_property
        def _get_average ( self ):
            s = self.scores
            return (float( reduce( lambda n1, n2: n1 + n2, s, 0 ) ) / len( s ))
            
Presumably this is much easier to write and understand that the following
equivalent code written without using *depends_on* and *cached_property*::
    
    class TestScores ( HasPrivateTraits ):
        
        scores  = List( Int )
        average = Property
        
        def _get_average ( self ):
            if self._average is None:
                s = self.scores
                self._average = (float( reduce( lambda n1, n2: n1 + n2, s, 0 ) )
                                 / len( s ))
            return self._average
            
        def _scores_changed ( self ):
            old, self._average = self._average, None
            self.trait_property_changed( 'average', old, self._average )
            
        def _scores_items_changed ( self ):
            self._scores_changed()
            
The *cached_property* decorator takes no arguments, and should simply be
written on the line preceding the property's *getter* method, as shown in the
previous example.

Use of the *cached_property* decorator also eliminates the need to add 
*cached = True* metadata to the property declaration, as was previously required
when using *depends_on* metadata with a cached property definition.
"""
from __future__ import division
from past.utils import old_div

#--<Imports>--------------------------------------------------------------------

from enthought.traits.api import *
from enthought.traits.ui.api import *

#--[TestScores Class]-----------------------------------------------------------

class TestScores(HasPrivateTraits):
    scores = List(Int)
    average = Property(depends_on='scores')

    @cached_property
    def _get_average(self):
        s = self.scores
        return (old_div(float(reduce(lambda n1, n2: n1 + n2, s, 0)), len(s)))


#--[Sample User Interface]------------------------------------------------------

class TestScoresHandler(ModelView):
    new_score = Int
    add_score = Button('Add New Score')

    view = View(
        VGroup(
            HGroup(
                Item('new_score'),
                Item('add_score', show_label=False)
            ),
            '_',
            Item('model.average',
                 label='Current average',
                 style='readonly')
        )
    )

    def _add_score_changed(self):
        """ Handles the user clicking the 'Add New Score' button by adding the
            current 'New score' value to the current list of scores.
        """
        self.model.scores.append(self.new_score)

#--[Example*]-------------------------------------------------------------------

# Create a sample TestScores object with some sample scores:
test_scores = TestScores(scores=[89, 93, 76, 84, 62, 96, 75, 81, 69, 90])

# Display the average:
print 'First average: ', test_scores.average

# Now add a few more late scores into the mix:
test_scores.scores.extend([85, 61, 70])

# And display the new average:
print 'Second average:', test_scores.average

#--<UI Demo>--------------------------------------------------------------------

# Create the demo UI:
demo = TestScoresHandler(model=test_scores)

