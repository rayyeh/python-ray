#!/usr/local/bin/python
# -*- coding :UTF-8 -*- 

import sys,cgi,httplib,os
from datetime import datetime
from xml.etree import ElementTree
from gevent.pywsgi import WSGIServer
from flask import Flask,request
from datetime import datetime
import logging
import logging.handlers

app=Flask(__name__)

dirname=os.path.dirname(__file__)

# create logger
logger = logging.getLogger('http-flask')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
#ch = logging.StreamHandler()
ch=logging.handlers.RotatingFileHandler(dirname.join('http-flask.log'), 'a', 4096, 5)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

@app.route('/TempPWD',methods=['POST','GET'])
def do_POST():
    if request.method == 'POST':
        cardno=request.form.get('cardnumber')
        pwd=request.form.get('password')
        
        try:
            conn=httplib.HTTPConnection('127.0.0.1',8080)
        except Exception:
            logger.error('Connect SMS server fail')
            return '<body>code=F999</body>\n' 
        
        SMS_text = '?'+'id='+cardno+'&pwd='+pwd+'&TEL=021234567&MSG="hello"'
        
        try:
            conn.request('GET',SMS_text)
        except Exception:
            logger.error('Send request to SMS server fail:')
            return '<body>code=F999</body>\n'

        # get  response from server
        try:
            response=conn.getresponse()
        except Exception:
            logger.error('Get SMS server response fail')
            return '<body>code=F999</body>\n'            
        
        # print '*** response.status:', response.status,'\tresponse reason:',response.reason
        data_received=response.read()

        # parse SMS response message
        msg=data_received.replace("Big5","utf-8")                
        tree=ElementTree.fromstring(msg)        
        for node in tree.iter():            
            if node.tag == 'SEND-RETN-DATE' : 
                sms_retn_data =node.text
            if node.tag == 'SEND-RETN-CODE':
                sms_retn_code =node.text
            if node.tag == 'SEND-RETN-CODE-DESC':
                sms_retn_code_desc = node.text
            if node.tag == 'MSG-ID':
                sms_msg_id = node.text
                
        # parse SMS response message and send to client       
        if sms_retn_code =='0000' :
            return '<body>code=W000</body>\n'
        else:
            return '<body>code=F999</body>\n'     
     
__version__ = '1.0.0'

if __name__ == '__main__':
    print 'Starting http server, use <Ctrl-C> to stop' 
       
    server_address = ('127.0.0.1', 8000)
    httpd=WSGIServer(server_address,app)
    print 'http server is running ....',server_address    
    httpd.serve_forever()
	
    #app.run('',8000,debug=True)
    