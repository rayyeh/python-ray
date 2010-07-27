# -*- coding: utf-8 -*-
''' The sample code for use Oracle , first install cx_Oracle'''
#cx_Oracle :version 5.0.2-10g.win32-py2.6

import sys
import cx_Oracle   #Use cx_Oracle module for oracle

#user/password@system
connection=cx_Oracle.Connection('UBLMST/UBLMST@UBLMST') 
cursor=connection.cursor()
  
try:
    cursor.execute('select * from merch')
    #print curs.description
    record=cursor.fetchone()  #fetch next row of a query result
    print record
    #print curs.fetchmany(10) #fetch next set of rows of query result
    connection.close() #close database
except cx_Oracle.DatabaseError,e:
    print e[0].context
    error=e.args
    print >>sys.stderr,"Oracle-Error-Code:",error.code
    print >>sys.stderr,"Oracle-Error-Messge:",error.message
