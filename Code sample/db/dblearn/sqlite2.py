#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('e2.sqlite')
c = conn.cursor()

# Create DB Table
# c.execute('''create table stocks
# (date text, trans text, symbol text,
# qty real, price real)''')

# insert multi row data 
for t in (('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
):
    c.execute('insert into stocks values (?,?,?,?,?)', t)

conn.commit()

#  read stocks Table and order by price 
c.execute('select * from stocks order by price')
for row in c:
    print row

c.execute('drop table stocks')
c.close()
