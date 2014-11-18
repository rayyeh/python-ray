# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.enable.component_editor import ComponentEditor
import numpy as np


class LinePlotTraits(HasTraits):
    plot = Instance(Plot)
    traits_view = View(
        Item('plot', editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self):
        super(LinePlotTraits, self).__init__()
        s = []
        t = []
        u = []
        for i in range(0, 50):
            j = i * i
            k = 2 * i * i
            s.append(i)
            t.append(j)
            u.append(k)

        x = np.array(s)
        y1 = np.array(t)
        y2 = np.array(u)
        plotdata = ArrayPlotData(x=x, y1=y1, y2=y2)
        plot = Plot(plotdata)
        plot.tools.append(PanTool(plot))
        plot.tools.append(ZoomTool(plot))

        plot.plot(("x", "y1"), type="line", color="red", name="t1")
        plot.plot(("x", "y2"), type="scatter", color="green", name="t2", marker="circle")
        plot.title = "Linar"
        plot.legend.visible = True  # 顯示 圖型說明
        plot.legend.align = 'ul'  # 圖型說明放在左上方
        self.plot = plot


if __name__ == "__main__":
    LinePlotTraits().configure_traits()