# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:38:58 2010

@author: rayyeh
"""

#!/usr/bin/env python
from __future__ import division

from enthought.traits.api import HasTraits, Instance, Array, on_trait_change, Range
from enthought.traits.ui.api import View, Item, Group
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.enable.component_editor import ComponentEditor
from numpy import *


class InterActive(HasTraits):
    n = Range(0, 100, 20)
    x = Array()
    y1 = Array()
    y2 = Array()
    plot = Instance(Plot)

    view = View(Group(
        Item('plot', editor=ComponentEditor(), show_label=False),
        Item('n', label='Set Range')),
                resizable=True, title='InterActive Plot')

    def __init__(self):
        super(InterActive, self).__init__()
        self.data = data = ArrayPlotData(x=self.x, y1=self.y1, y2=self.y2)

        self._update_n()

        plot = Plot(data, resizable='v')
        plot.tools.append(PanTool(plot))
        plot.tools.append(ZoomTool(plot))
        plot.legend.visible = True  # 顯示 圖型說明
        plot.legend.align = 'ul'  # 圖型說明放在左上方
        plot.title = "X Function"
        plot.value_scale = "log"
        self.render1 = plot.plot(
            ('x', 'y1'), type='scatter', color='blue', name='X*X')
        self.render2 = plot.plot(
            ('x', 'y2'), type='line', color='red', name='X*X')
        self.plot = plot

    @on_trait_change('n')
    def _update_n(self):
        i = []
        j = []
        k = []
        for cnt in range(self.n):
            i.append(cnt)
            j.append(cnt * cnt)
            k.append(cnt ** 2)
        self.data.set_data('x', i)
        self.data.set_data('y1', j)
        self.data.set_data('y2', k)


if __name__ == '__main__':
    InterActive().configure_traits()
