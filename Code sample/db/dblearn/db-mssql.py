''' Demo: How to connect to MSSQL, first,need to install pymssql'''

import pymssql

# connect to Database
con = pymssql.connect(host='192.168.11.62',user='ray',password='ray',database='ray')
cur = con.cursor()

#execute SQL command
#cur.execute('select * from Response')
#data=cur.fetchone()
#print data
#for x in data:
#    print x

#Drop DB table 
query="drop table pymssql;"
cur.execute(query)
print "drop table: %d" % cur.rowcount    

#Create DB table 
#query="create table pymssql (no int, fno float, comment varchar(50));"
#cur.execute(query)
#print "create table: %d" % cur.rowcount

#Insert data into DB 
#for x in range(10):
#    query="insert into pymssql (no,fno,comment) values (%d,%d.%d,'%dth comment');" #% (x+1,x+1,x+1,x+1)
#    ret=cur.execute(query)
#    print "insert table: %d" % cur.rowcount
    

#Update data into DB
#for x in range(10):
#    query="update pymssql set comment='%dth hahaha.' where no = %d" % (x+1,x+1)
#    ret=cur.execute(query)
#    print "update table: %d" % cur.rowcount
    


#query="EXEC sp_tables; select * from pymssql;"
#for x in range(10):
#    cur.execute(query)
#    while 1:
#	print cur.fetchall()
#	if 0 == cur.nextset():
#	    break
	
con.commit()
con.close()
