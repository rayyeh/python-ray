# -*- coding: utf-8 -*-
"""
Created on Tue May 04 10:03:17 2010

@author: rayyeh
"""

from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.enable.component_editor import ComponentEditor
from numpy import cos, linspace, sin


class OverlappingPlot(HasTraits):
    plot = Instance(Plot)
    traits_view = View(
        Item('plot', editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self):
        super(OverlappingPlot).__init__(int)
        x = linspace(-14, 14, 100)
        y = x / 2 * sin(x)
        y2 = cos(x)
        plotdata = ArrayPlotData(x=x, y=y, y2=y2)
        plot = Plot(plotdata)
        plot.plot(("x", "y"), type="scatter", color="blue")
        plot.plot(("x", "y2"), type="line", color="red")
        self.plot = plot


if __name__ == "__main__":
    OverlappingPlot().configure_traits()