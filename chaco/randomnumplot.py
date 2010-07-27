# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.enable.component_editor import ComponentEditor
import numpy as np
import random 

class LinePlotTraits(HasTraits):
    plot = Instance(Plot)
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")
        
    def __init__(self):
        super(LinePlotTraits ,self).__init__()
        s=[]
        t=[]
        u=[]
        for i in range(1,1000):
            
            random.seed(i)
            j=random.random()
            print 'num %s, ran_num %s' %(i,j)
            s.append(i)
            t.append(j)
            
        x=np.array(s)
        y1=np.array(t)
        plotdata = ArrayPlotData(x=x, y1=y1)
        plot=Plot(plotdata)
        plot.tools.append(PanTool(plot))
        plot.tools.append(ZoomTool(plot))
        
        plot.plot(("x","y1"), type="scatter",color="green",\
                 maker="CIRCLE_MARKER",marker_size = 1,name="t1")
        plot.title= "Random"
        #plot.legend.visible = True  #顯示 圖型說明
        plot.legend.align='ul' # 圖型說明放在左上方
        self.plot=plot
        
if __name__ == "__main__":
    LinePlotTraits().configure_traits()