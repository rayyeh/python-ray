# -*- coding: utf-8 -*- 
"""
    AcsSMS-
    The application written as Flask tutorial with
    Flask and MongoDB

    :copyright: (c) 2012 by Ray Yeh.
    :license: BSD, see LICENSE for more details.
"""
from future import standard_library
standard_library.install_aliases()
from builtins import str

from __future__ import with_statement
import sys
import http.client
import os
import datetime
from xml.etree import ElementTree
import logging
from logging.handlers import RotatingFileHandler

from gevent.pywsgi import WSGIServer

# from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack
import pyodbc
from pymongo import MongoClient

_version_ = 1.0
_author_ = 'Ray Yeh'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ACSSMS_SETTINGS', silent=True)

# configure logger
dirname = os.path.dirname(__file__)
logger = logging.getLogger(app.config['LOGGER'])
formatter = logging.Formatter \
    ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = RotatingFileHandler(dirname.join('http-flask.log'), 'a', 4096, 5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# configure MongoDB,db='sms',collections='tranlog'
connection = MongoClient(app.config['MONGODB_HOST'],
                         app.config['MONGODB_PORT'])
db = connection['sms']
db.authenticate(app.config['MONGODB_USER'], app.config['MONGODB_PWD'])
tranlogs = db.tranlog


def con_MSSQL():
    try:
        mssql_constring = 'DRIVER={SQL Server};\
        SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' \
                          % (app.config['MSSQL_IP'], app.config['MSSQL_DB'], \
                             app.config['MSSQL_USER'], app.config['MSSQL_PWD'])
        mssql_con = pyodbc.connect(mssql_constring)
    except pyodbc.Error as err:
        logger.error(err)
    mssql_cursor = mssql_con.cursor()
    return mssql_cursor, mssql_con


def write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                  sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                  resp):
    trandate = str(datetime.date.today())
    trantime = datetime.datetime.now()
    tranlog = {'trandate': trandate,
               'trantime': trantime,
               'pan': pan,
               'pwd': pwd,
               'tel': tel,
               'retndate': sms_retn_date,
               'retncode': sms_retn_code,
               'retndesc': sms_retn_code_desc,
               'msgid': sms_msg_id,
               'resp': resp}
    tranlogs.insert(tranlog, safe=True)


@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    db.close()
    mssql_conn.close()


@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        cardno = str(request.form.get('cardnumber'))
        if cardno <> '':
            entries = list(tranlogs.find({'pan': cardno}).sort("trantime", -1))
            flash_msg = 'Show by card number :' + cardno
            flash(flash_msg)
            return render_template('show_entries.html', entries=entries)
        else:
            flash('Please enter card number')
    return render_template('home.html')


@app.route('/show')
def show_entries():
    entries = list(tranlogs.find().sort("trantime", -1).limit(100))
    flash(u'show top 100')
    return render_template('show_entries.html', entries=entries)


#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404

@app.route('/TempPWD', methods=['POST', 'GET'])
def do_POST():
    trandate = trantime = None
    pan = pwd = tel = sms_retn_date = sms_retn_code = ''
    sms_retn_code_desc = sms_msg_id = resp = ''

    if request.method == 'POST':
        pan = request.form.get('cardnumber')
        pwd = request.form.get('password')

        # connect MSSQL to get tel by pan
        try:
            mssqlcursor, mssqlcon = con_MSSQL()
        except:
            logger.error('Connect MSSQL server fail')
            tel = ''
            resp = "W010"
            write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                          sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                          resp)
            return '<body>code=W010</body>\n'


        # connection successful ,then  query     
        mssqlcursor.execute("select * from REJECT where cardno=?", pan)
        row = mssqlcursor.fetchone()
        if row == None:
            logger.error('Can not find pan in SQL,PAN=' + str(pan))
            tel = ''
            resp = "W010"
            write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                          sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                          resp)
            return '<body>code=W010</body>\n'
        else:
            tel = row[4]
        mssqlcon.close()

        #connect to SMS server        
        try:
            conn = http.client.HTTPConnection('127.0.0.1', 8080)
        except Exception:
            logger.error('Connect SMS server fail')
            return '<body>code=F999</body>\n'

        SMS_text = '?' + 'id=' + pan + '&pwd=' + pwd + '&TEL=' + tel + '&MSG="hello"'

        try:
            conn.request('GET', SMS_text)
        except Exception:
            logger.error('Send request to SMS server fail:')
            resp = 'F999'
            write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                          sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                          resp)
            return '<body>code=F999</body>\n'

            # get  response from server
        try:
            response = conn.getresponse()
        except Exception:
            logger.error('Get SMS server response fail')
            resp = 'F999'
            write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                          sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                          resp)
            return '<body>code=F999</body>\n'

            # parse SMS response message
        data_received = response.read()
        msg = data_received.replace("Big5", "utf-8")
        tree = ElementTree.fromstring(str(msg))
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
            write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                          sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                          resp)
            return '<body>code=W000</body>\n'
        else:
            resp = 'F999'
            write_Tranlog(trandate, trantime, pan, pwd, tel, sms_retn_date, \
                          sms_retn_code, sms_retn_code_desc, sms_msg_id, \
                          resp)
            return '<body>code=F999</body>\n'


if __name__ == '__main__':
    print 'Starting http server, use <Ctrl-C> to stop'
    server_address = ('127.0.0.1', 8000)
    httpd = WSGIServer(server_address, app)
    httpd.serve_forever()
    print 'http server is running ....', server_address

    #app.run('',8000,debug=True)
    
