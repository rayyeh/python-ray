# -*- coding:utf-8 -*-
"""
Created on 2010/6/10
Demo: TableEditor  and use Sqlite DB
@author: rayyeh
"""
from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.tabular_adapter import *
import sqlite3


class ROW(HasTraits):
    date = Str
    trans = Str
    symbol = Str
    qty = Float
    price = Float

# TabularEditor Definition  
table_editor = TableEditor(
    columns=[ObjectColumn(name='date', width=0.2),
             ObjectColumn(name='trans', width=0.2),
             ObjectColumn(name='symbol', width=0.1),
             ObjectColumn(name='qty', horizontal_alignment='center'),
             ObjectColumn(name='price')],
    orientation='vertical',
    deletable=False,
    sort_model=True,
    auto_size=False,
    edit_view=View(
        Group('date', 'trans', 'symbol', 'qty', 'price', \
              show_border=True
        ),
        resizable=True
    ),
    row_factory=ROW
)


class DB(HasTraits):
    show = Button()
    rowdata = List(ROW)
    view = View(Group(Item('rowdata',
                           editor=table_editor)),
                Item('show'),
                # kind="modal",
                # 'panel'
                # 'subpanel'
                #'modal'
                #'nonmodal'
                #'livemodal'
                #'live'
                #'popup'
                #'popover'
                #'info'
                #'wizard'
                buttons=OKCancelButtons,
                width=300, height=300,
                resizable=True,
                title='TableEditor Demo'
    )

    def _show_fired(self):
        conn = sqlite3.connect('D:\python-ray\dblearn\example.sqlite')
        c = conn.cursor()
        c.execute('select * from stocks order by price')

        rows = []
        for row in c:
            rawdata = ROW(date=row[0], trans=row[1], symbol=row[2], qty=row[3], price=row[4])
            rows.append(rawdata)
        c.close()
        self.rowdata = rows


demo = DB()
if __name__ == '__main__':
    demo.configure_traits()



