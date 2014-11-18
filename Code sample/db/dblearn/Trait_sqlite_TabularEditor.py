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


# -- Tabular Adapter Definition -------------------------------------------------
class DBAdapter(TabularAdapter):
    columns = [('Date', 'date'),
               ('Trans', 'trans'),
               ("Symbol", 'symbol'),
               ('QTY', 'qty'),
               ('Price', 'price')
    ]
    font = 'Courier 10'
    qty_alignment = Constant('right')
    price_alignment = Constant('right')


# -- Tabular Editor Definition --------------------------------------------------
tabular_editor = TabularEditor(
    adapter=DBAdapter(),
    operations=['delete', 'insert', 'append', 'edit', 'move'],
)


class DB(HasTraits):
    show = Button()
    rowdata = List(ROW)
    view = View(Group(Item('rowdata', id='table', show_label=False,
                           editor=tabular_editor)),
                Item('show'),
                kind="nonmodal",
                # 'panel'
                #'subpanel'
                #'modal'
                #'nonmodal'
                #'livemodal'
                #'live'
                #'popup'
                #'popover'
                #'info'
                #'wizard'
                buttons=OKCancelButtons,
                width=400, height=300,
                resizable=True,
                title='TabularEditor Demo'
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



