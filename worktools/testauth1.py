# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool,SaveTool
from enthought.enable.component_editor import ComponentEditor
import numpy as np
import random, os


class TestAuthTraits(HasTraits):
    authnumlist1=[]
    authnumlist2=[]
    timelist1=[]
    timelist2=[]
    time1=''
    time2=''
    cnt1=0
    cnt2=0
    plot = Instance(Plot)
    
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=800, height=600, resizable=True, title="Chaco Plot")
        
    def __init__(self):
        super(TestAuthTraits,self).__init__()
        
        for hh in range(22,24):
            for mm in range(0,60):
                for ss in range(0,60):
                    for ms  in range(0,10):
                        secnew=(((hh*3600+mm*60+ss)*10)+ms)+1 
                        secold=mm*10000+ss*1000+ms*10+1
                                                 
                        self.authnumlist1.append(secnew) 
                        self.authnumlist2.append(secold)
                                               
                        self.cnt1=self.cnt1+1
                        # X axis                                               
                        time1=ms+ss*10+mm*1000+hh*100000                        
                        self.timelist1.append(time1)                           
                  
                
        x1=np.array(self.timelist1)
        y1=np.array(self.authnumlist1)  
        y2=np.array(self.authnumlist2)       
        
        plotdata = ArrayPlotData(x1=x1,y1=y1,y2=y2)
        plot=Plot(plotdata)
        plot.tools.append(PanTool(plot))
        plot.tools.append(SaveTool(plot))
        #plot.tools.append(ZoomTool(plot))
        plot.legend.visible = True  
        plot.legend.align='ul'        
        plot.plot(("x1","y1"), type="scatter",color='red',name='new',marker='dot',marker_size=2)        
        plot.plot(("x1","y2"), type="scatter",color='green',name='current',marker='circle',marker_size=2)  
        self.plot=plot
        
        print u'時間筆數 cnt 1:',self.cnt1
        #print u'時間筆數 cnt 2:',self.cnt2
        print 'New Last time(hh_mm_ss_ms) :',time1               
        
        

if __name__ == "__main__":
    TestAuthTraits().configure_traits()
         