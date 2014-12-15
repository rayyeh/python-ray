from builtins import str
from builtins import range
# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.enable.component_editor import ComponentEditor
import numpy as np


class TestAuthTraits(HasTraits):
    authnumlist = []
    timelist = []
    timex = ''
    plot = Instance(Plot)

    traits_view = View(
        Item('plot', editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self):
        super(TestAuthTraits, self).__init__()
        # for hh in range(1,2):
        for mm in range(0, 60):
            for ss in range(0, 60):
                for ms in range(1, 101):
                    sec = ms + 100 * ss + mm * 1000
                    self.authnumlist.append(sec)
                    timex = str(mm) + str(ss) + str(ms)
                    self.timelist.append(int(timex))

        x = np.array(self.timelist)
        y = np.array(self.authnumlist)

        plotdata = ArrayPlotData(x=x, y=y)
        plot = Plot(plotdata)
        plot.tools.append(PanTool(plot))
        plot.tools.append(ZoomTool(plot))
        plot.legend.visible = True
        plot.legend.align = 'ul'
        plot.plot(("x", "y"), type="scatter", color='red')
        self.plot = plot


if __name__ == "__main__":
    TestAuthTraits().configure_traits()
