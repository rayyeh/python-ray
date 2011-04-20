   #!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# example database and Python in the same folder
conn = sqlite3.connect('example.sqlite')

c = conn.cursor()

# Create DB Table
c.execute('''create table stocks
  (date text, trans text, symbol text,
   qty real, price real)''')

# Insert one  row data
c.execute("""insert into stocks
  values ('2006-01-05','BUY','RHAT',100,35.14)""")

#  commit and save into DB
conn.commit()


# close DB
c.close()
