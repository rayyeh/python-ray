# -*- coding:utf-8 -*-
"""
Created on 2010/6/10

@author: rayyeh
"""
from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.tabular_adapter import *
import sqlite3

class ViewAdapter(TabularAdapter):
        
        conn = sqlite3.connect('d:\python-ray\code sample\db\example.sqlite')
        c = conn.cursor()
        columns = [ ( 'Image Name', 'image' ) ]
        c.execute('select * from stocks order by price')
        row=c.fetchone()
        row_data=row
        print row

class DB(HasTraits):   
    show=Button()
    view=View(Group(Item('row_data',
                    editor=TabularEditor(
                        adapter=ViewAdapter(),
                        horizontal_lines = False)),
                    orientation='vertical',
                    #layout='split'
                    #columns=2
                    ),
                buttons=LiveButtons,
                width=300,height=300, 
                resizable=True,              
                title='SQLITE DB'                    
                )
        
        #example database and Python in the same folder
 
       
 
    

       
a=DB()
a.configure_traits()



