# -*- coding: utf-8 -*- 
"""
    AcsSMS-
    The example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2012 by Ray Yeh.
    :license: BSD, see LICENSE for more details.
"""

from __future__ import with_statement
import sys,os,urllib,urllib2
from collections import OrderedDict
from datetime import datetime,date,time
from xml.etree import ElementTree
from gevent.pywsgi import WSGIServer
import logging
from logging.handlers import RotatingFileHandler
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
import pyodbc

_version_ =1.0
_author_ ='Ray Yeh'     

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
#set ACSSMS_SETTINGS=settings.ini
app.config.from_envvar('ACSSMS_SETTINGS', silent=True)

# configure logger
dirname=os.path.dirname(__file__)
logger = logging.getLogger(app.config['LOGGER'])
formatter = logging.Formatter\
    ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = RotatingFileHandler(dirname.join('http-flask.log'), 'a', 4096, 5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
        
def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('acssms.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'acssms_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return top.sqlite_db

def con_MSSQL():
    try:
        mssql_constring='DRIVER={SQL Server};\
        SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'\
        %(app.config['MSSQL_IP'],app.config['MSSQL_DB'],\
          app.config['MSSQL_USER'],app.config['MSSQL_PWD'])
        mssql_con = pyodbc.connect(mssql_constring)        
    except pyodbc.Error as err:
        logger.error(err)
    mssql_cursor = mssql_con.cursor()
    return mssql_cursor,mssql_con

@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'acssms_db'):
        top.sqlite_db.close()

        
@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':        
        cardno=str(request.form.get('cardnumber'))
        
        if cardno <> '':            
            db = get_db()
            db.text_factory = sqlite3.OptimizedUnicode
            cur = db.execute('select count(1) from smslog where pan =?',(cardno,))
            (number_of_rows,)=cur.fetchone()
            cur = db.execute('select trantime,pan,pwd,tel,retndate,retncode,\
            retndesc,msgid,resp from smslog where pan =? \
            order by trantime desc limit ?',(cardno,number_of_rows))
            entries=[]
            count = 0
            for row in cur.fetchall():
                count = count + 1 
                entry=dict(no=count,trantime=row[0], pan=row[1],pwd=row[2],tel=row[3],\
                     retndate=row[4],retncode=row[5],retndesc=row[6],\
                      msgid=row[7],resp=row[8])
                entries.append(entry)
            
            #entries = [dict(no=no+1,trantime=row[0], pan=row[1],pwd=row[2],tel=row[3],\
            #           retndate=row[4],retncode=row[5],retndesc=row[6],\
            #           msgid=row[7],resp=row[8]) for row in cur.fetchall()]
            
            flash('Show by card number')
            return render_template('show_entries.html', entries=entries)
        else:
            flash('Please enter card number')
    return render_template('home.html')
	
@app.route('/show')
def show_entries():
    db = get_db()
    cur = db.execute('select trantime,pan,pwd,tel,retndate,retncode,\
    retndesc,msgid,resp from smslog \
    order by trantime desc limit 100')
    entries=[]
    count = 0
    for row in cur.fetchall():
        count = count + 1
        entry=dict(no=count,trantime=row[0], pan=row[1],pwd=row[2],tel=row[3],\
                   retndate=row[4],retncode=row[5],retndesc=row[6],\
                   msgid=row[7],resp=row[8])
        entries.append(entry)
    #entries = [dict(trantime=row[0], pan=row[1],pwd=row[2],tel=row[3],\
    #                retndate=row[4],retncode=row[5],retndesc=row[6],\
    #                msgid=row[7],resp=row[8]) for row in cur.fetchall()]
    
    flash(u'顯示前  100 筆交易 -- 依交易時間 由近而遠')
    return render_template('show_entries.html', entries=entries)

@app.route('/TempPWD',methods=['POST','GET'])
def do_POST():
    trandate=trantime=None
    pan=pwd=tel=sms_retn_date=sms_retn_code=''
    sms_retn_code_desc=sms_msg_id=resp=''
    trandate = date.today()
    trantime = datetime.now()       
    
    def do_LOG(logtext=[]):        
        db=get_db()
        db.execute('insert into smslog (trandate,trantime,pan,pwd,tel,\
                    retndate,retncode,retndesc,msgid,resp)\
                    values (?,?,?,?,?,?,?,?,?,?)',logtext)
        db.commit()              
   
    if request.method == 'POST':                        
        pan=request.form.get('cardnumber')
        pwd=request.form.get('password')        
                
        # connect MSSQL to get tel by pan
        try:
            mssqlcursor,mssqlcon=con_MSSQL()
        except:
            logger.error('Connect MSSQL server fail')
            tel=''
            resp="W010"
            trantime = datetime.now()
            logdata=[trandate,trantime,pan,pwd,tel,sms_retn_date,sms_retn_code,\
                     sms_retn_code_desc,sms_msg_id,resp]
            do_LOG(logdata)
            #mssqlcon.close() 
            return '<body>code=W010</body>\n'
        
        # connection successful ,then  query     
        mssqlcursor.execute("select * from REJECT where cardno=?",pan)
        row=mssqlcursor.fetchone()
        if row == None:
            tel=''
            resp="W010"
            trantime = datetime.now()
            logdata=[trandate,trantime,pan,pwd,tel,sms_retn_date,sms_retn_code,\
                     sms_retn_code_desc,sms_msg_id,resp]
            do_LOG(logdata)
            return '<body>code=W010</body>\n'
        else:   
            tel=row[4]
        mssqlcon.close() 
                
        #connect to SMS server
        data=OrderedDict();
        data['ID']=pan
        data['PWD']=pwd
        data['TEL']=tel
        data['MSG']='Hello' 
        url_values=urllib.urlencode(data)
        url='http://127.0.0.1:8080'
        full_url=url+'?'+url_values
        print full_url
        response=urllib2.urlopen(full_url)
        data_received=response.read()        
        
        # parse SMS response message
        msg=data_received.replace('Big5','utf-8')
        tree=ElementTree.fromstring(str(msg))        
        for node in tree.iter():            
            if node.tag == 'SEND-RETN-DATE' : 
                sms_retn_date =node.text                
            if node.tag == 'SEND-RETN-CODE':
                sms_retn_code =node.text                
            if node.tag == 'SEND-RETN-CODE-DESC':
                sms_retn_code_desc = node.text
            if node.tag == 'MSG-ID':
                sms_msg_id = node.text
        
                
        # parse SMS response message and send to client       
        if sms_retn_code =='0000' :
            resp='W000'
            trantime = datetime.now()
            logdata=[trandate,trantime,pan,pwd,tel,sms_retn_date,sms_retn_code,\
                     sms_retn_code_desc,sms_msg_id,resp]
            do_LOG(logdata)
            return '<body>code=W000</body>\n'
        else:
            resp='F999'
            trantime = datetime.now()
            logdata=[trandate,trantime,pan,pwd,tel,sms_retn_date,sms_retn_code,\
                     sms_retn_code_desc,sms_msg_id,resp]
            do_LOG(logdata)
            return '<body>code=F999</body>\n'     
     

if __name__ == '__main__':
    print 'Starting http server, use <Ctrl-C> to stop'        
    server_address = ('127.0.0.1', 8000)
    #httpd=WSGIServer(server_address,app)
    #httpd.serve_forever()
    print 'http server is running ....',server_address 
    app.run('',8000,debug=True)
    
