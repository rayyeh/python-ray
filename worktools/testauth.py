# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.chaco.tools.api import PanTool, ZoomTool
from enthought.enable.component_editor import ComponentEditor
import numpy as np
import random, os, Gnuplot


class TestAuthTraits(HasTraits):
    twonum=0
    threenum=0
    fournum=0
    fivenum=0
    twonumlist=[]
    threenumlist=[]
    fournumlist=[]
    fivenumlist=[]
    time2=[]
    time3=[]
    time4=[]
    time5=[]    
    timex=''
    plot = Instance(Plot)
    
    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")
        
    def __init__(self):
        super(TestAuthTraits,self).__init__()
        for mm in range(0,60):
            for ss in range(0,60):
                for ms  in range(1,101):
                    x=mm*10 + ss                    
                    y=str(x)
                    j=str(ms)
                    authnum=y+j               
                    
                    if j[0:1]==j[1:2]:             
                        self.twonum=self.twonum+1
                        self.twonumlist.append(int(authnum))
                        timex=str(mm)+str(ss)+str(ms)
                        self.time2.append(int(timex))
                        
                    if j[0:1]==j[1:2] and j[1:2]==y[2:3]:
                        self.threenum=self.threenum+1
                        self.threenumlist.append(int(authnum))
                        timex=str(mm)+str(ss)+str(ms)
                        self.time3.append(int(timex))
                                                  
                    if j[0:1]==j[1:2]and j[1:2]==y[2:3] and  y[1:2]==y[2:3]:
                        self.fournum=self.fournum+1
                        self.fournumlist.append(int(authnum))
                        timex=str(mm)+str(ss)+str(ms)
                        self.time4.append(int(timex))
                        
                    if j[0:1]==j[1:2]and j[1:2]==y[2:3] and  y[1:2]==y[2:3] and \
                        y[0:1]==y[1:2]:
                        self.fivenum=self.fivenum+1
                        self.fivenumlist.append(int(authnum))
                        timex=str(mm)+str(ss)+str(ms)
                        self.time5.append(int(timex))
                        
        p2=np.array(self.time2)
        p3=np.array(self.time3)
        p4=np.array(self.time4)
        p5=np.array(self.time5)
        q2=np.array(self.twonumlist)
        q3=np.array(self.threenumlist)
        q4=np.array(self.fournumlist)
        q5=np.array(self.fivenumlist)
        
        
        plotdata = ArrayPlotData(x2=p2,x3=p3,x4=p4,x5=p5,\
                                 y2=q2,y3=q3,y4=q4,y5=q5)
        plot=Plot(plotdata)
        plot.tools.append(PanTool(plot))
        plot.tools.append(ZoomTool(plot))
        plot.legend.visible = True  
        plot.legend.align='ul' 
        plot.plot(("x2","y2"), type="scatter",color='red')
        plot.plot(("x3","y3"), type="scatter",color='blue')
        plot.plot(("x4","y4"), type="scatter",color='green')
        plot.plot(("x5","y5"), type="scatter",color='pink')
        
        self.plot=plot
             
             
        print 'Twonum:%s'%(self.twonum)
        print 'Threenum:%s'%(self.threenum)
        print 'Fournum:%s'%(self.fournum)
        print 'Fivenum:%s'%(self.fivenum)
        

if __name__ == "__main__":
    TestAuthTraits().configure_traits()
         