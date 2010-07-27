# -*- coding:utf-8 -*-
from enthought.traits.api import HasTraits,Property,Float \
            ,cached_property,Any,on_trait_change,Range 
from enthought.traits.ui.api import Item

# A re-usable trait for specifying volumes
volume_trait = Range(0.0, 11.0, value=5.0)

class Amplifier(HasTraits):
	volume = volume_trait	
	def _volume_changed(self, old, new):
		print "amplifier volume:", new
		
class ControlPanel(HasTraits):
	guitar_volume = volume_trait
	def _guitar_volume_changed(self, old, new):
		print "control panel guitar volume:", new

guitar_amplifier = Amplifier()
control_panel = ControlPanel()

# setup bi-directional synchronization
control_panel.sync_trait('guitar_volume', guitar_amplifier, 'volume')
control_panel.guitar_volume = 1.0