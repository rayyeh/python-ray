# -*- coding: utf-8 -*- 
"""
    AcsSMS
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2012 by Ray Yeh.
    :license: BSD, see LICENSE for more details.
"""

from __future__ import with_statement
import sys
import httplib
import os
from datetime import datetime, date, time
from xml.etree import ElementTree
import logging
from logging.handlers import RotatingFileHandler
from sqlite3 import dbapi2 as sqlite3

from gevent.pywsgi import WSGIServer
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack


_version_ = 1.0
_author_ = 'Ray Yeh'

# configuration
DATABASE = 'acssms.db'
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

dirname = os.path.dirname(__file__)

# configure logger 
logger = logging.getLogger('http-flask')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = RotatingFileHandler(dirname.join('http-flask.log'), 'a', 4096, 5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

today = date.today()
now = datetime.now()


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


@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'acssms_db'):
        top.sqlite_db.close()


@app.route('/TempPWD', methods=['POST', 'GET'])
def do_POST():
    if request.method == 'POST':
        cardno = request.form.get('cardnumber')
        pwd = request.form.get('password')
        today = date.today()
        now = datetime.now()

        # try:
        #    conn=httplib.HTTPConnection('127.0.0.1',8080)
        #except Exception:
        #    logger.error('Connect SMS server fail')
        #    return '<body>code=F999</body>\n' 
        tel = '021234567'
        SMS_text = '?' + 'id=' + cardno + '&pwd=' + pwd + '&TEL=' + tel + '&MSG="hello"'

        #try:
        #    conn.request('GET',SMS_text)
        #except Exception:
        #    logger.error('Send request to SMS server fail:')
        #    db=get_db()
        #    db.execute('insert into smslog (trandate,trantime,pan,pwd,tel,retndate,retncode,retndesc,msgid,resp)\
        #        values (?,?,?,?,?,?,?,?,?,?)',
        #        [today,now,cardno,pwd,'','','','','',''])            
        #    db.commit()
        #    return '<body>code=F999</body>\n'   

        # get  response from server
        #try:
        #    response=conn.getresponse()
        #except Exception:
        #    logger.error('Get SMS server response fail')
        #    db=get_db()
        #    db.execute('insert into smslog (trandate,trantime,pan,pwd,tel,retndate,retncode,retndesc,msgid,resp)\
        #        values (?,?,?,?,?,?,?,?,?,?>)',
        #        [today,now,cardno,pwd,tel,'','','','',''])            
        #    db.commit()
        #    return '<body>code=F999</body>\n'            

        # print '*** response.status:', response.status,'\tresponse reason:',response.reason
        #data_received=response.read()
        data_received = '<SEND> <TxnID>SENDMSG<SEND-RETN-DATE>20120101123456\
                   </SEND-RETN-DATE>\
                     <SEND-RETN-CODE>0000</SEND-RETN-CODE>\
                    <SEND-RETN-CODE-DESC>中文</SEND-RETN-CODE-DESC>\
                    </TxnID><SYSMSG><MSG-ID>123456 </MSG-ID><MSG-DESC></MSG-DESC></SYSMSG></SEND>'

        # parse SMS response message
        msg = data_received.replace("Big5", "utf-8")
        tree = ElementTree.fromstring(msg)
        for node in tree.iter():
            if node.tag == 'SEND-RETN-DATE':
                sms_retn_date = node.text
            if node.tag == 'SEND-RETN-CODE':
                sms_retn_code = node.text
            if node.tag == 'SEND-RETN-CODE-DESC':
                sms_retn_code_desc = node.text
            if node.tag == 'MSG-ID':
                sms_msg_id = node.text

        # parse SMS response message and send to client       
        if sms_retn_code == '0000':
            resp = 'W000'
            db = get_db()
            db.execute('insert into smslog (trandate,trantime,pan,pwd,tel,retndate,retncode,retndesc,msgid,resp)\
                values (?,?,?,?,?,?,?,?,?,?)',
                       [today, now, cardno, pwd, tel, sms_retn_date, sms_retn_code, sms_retn_code_desc, sms_msg_id,
                        resp])
            db.commit()
            return '<body>code=W000</body>\n'
        else:
            resp = 'F999'
            db = get_db()
            db.execute('insert into smslog (trandate,trantime,pan,pwd,tel,retndate,retncode,retndesc,msgid,resp)\
                values (?,?,?,?,?,?,?,?,?,?)',
                       [today, now, cardno, pwd, tel, sms_retn_date, sms_retn_code, sms_retn_code_desc, sms_msg_id,
                        resp])
            db.commit()
            return '<body>code=F999</body>\n'


__version__ = '1.0.0'

if __name__ == '__main__':
    print 'Starting http server, use <Ctrl-C> to stop'

    server_address = ('127.0.0.1', 8000)
    httpd = WSGIServer(server_address, app)
    httpd.serve_forever()
    print 'http server is running ....', server_address

    # app.run('',8000,debug=True)
    
