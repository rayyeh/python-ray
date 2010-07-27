#!/usr/bin/env python
from __future__ import division

from enthought.traits.api import HasTraits,Instance,Int,Array,Float,Property,on_trait_change,Range
from enthought.traits.ui.api import View,Item,Group
from enthought.chaco.api import Plot,ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.enable.component_editor import ComponentEditor

import numpy as np
from numpy.random import randn
from scipy.interpolate import UnivariateSpline


class Smoother(HasTraits):
    s = Range(0,1e6,250.0) 
    k = Range(2,4,3)
    
    p = Range(0.0,10.0,0.0)
    A = Range(0.0,100.0,1.0)
    n = Int(250)
    lower = Range(0.0,20.0,0.0,exclude_low=True)
    upper = Range(0.0,20.0,2.0,exclude_low=True) 
    x = Array()
    y = Array()    
    spline=Array()    
    plot = Instance(Plot)
    
    view = View(Group(
                Item('plot',editor=ComponentEditor(),show_label=False),
                Item('k',label='Spline Degree'),
                Item('s',label='Spline Smoothing'),
                Item('A',label='Noise Amplitude'),
                Item('p',label='Power-law index'),
                Item('n',label='Number of points'),
                Item('lower',label='X minimum'),
                Item('upper',label='X maximum')),
                resizable=True,title='Spline Explorer')
    
    def __init__(self):
        super(Smoother, self).__init__()
        self.data = data = ArrayPlotData(x=self.x,y=self.y,spline=self.spline)
        
        self._update_x()
        self._update_y()
        self._update_sobject()        
        
        plot = Plot(data,resizable='v')
        plot.tools.append(PanTool(plot))
        plot.tools.append(ZoomTool(plot))
        
        self.render1 = plot.plot(('x','y'),type='scatter',color='blue')
        self.render2 = plot.plot(('x','spline'),type='line',color='red')
        self.plot = plot
        
        
    @on_trait_change('n,lower,upper')
    def _update_x(self):
        self.x = np.linspace(self.lower,self.upper,self.n)
        self.data.set_data('x',self.x)
        
    @on_trait_change('A,p,x')
    def _update_y(self):
        self.y = randn(len(self.x))*self.A+self.x**self.p - 1
        self.data.set_data('y',self.y)
    
    @on_trait_change('s')
    def _update_spline(self):
        self.splineobj.set_smoothing_factor(self.s)
        self.spline = self.splineobj(self.x)
        self.data.set_data('spline',self.spline)
    
    @on_trait_change('x,k,y')
    def _update_sobject(self):
        self.splineobj = UnivariateSpline(self.x,self.y,s=self.s,k=self.k)
        self.spline = self.splineobj(self.x)
        self.data.set_data('spline',self.spline)

if __name__ == '__main__':
    Smoother().configure_traits()