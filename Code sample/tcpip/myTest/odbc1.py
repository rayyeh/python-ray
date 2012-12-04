import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.28.251.11;DATABASE=S23_CISSUER\
           ;UID=ray;PWD=ray@3931')
cursor = cnxn.cursor()

cursor.execute("select * from TestCase")
row = cursor.fetchone()
print row[0]
print row[1]
print row[2]
print row[3]
