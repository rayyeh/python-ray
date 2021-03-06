from __future__ import division
from past.utils import old_div
# -------------------------------------------------------------------------------
#
#  Copyright (c) 2007, Enthought, Inc.
#  All rights reserved.
# 
#  This software is provided without warranty under the terms of the BSD
#  license included in /LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
# 
#-------------------------------------------------------------------------------

# cached_prop.py - Example of @cached_property decorator 

#--[Imports]--------------------------------------------------------------------
from enthought.traits.api import HasPrivateTraits, List, Int, \
    Property, cached_property

#--[Code]-----------------------------------------------------------------------

class TestScores(HasPrivateTraits):
    scores = List(Int)
    average = Property(depends_on='scores')

    @cached_property
    def _get_average(self):
        s = self.scores
        return (old_div(float(reduce(lambda n1, n2: n1 + n2, s, 0)), len(s)))

