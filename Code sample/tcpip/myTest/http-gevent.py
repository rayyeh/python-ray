#!/usr/local/bin/python
# -*- coding :UTF-8 -*- 

import sys,cgi,httplib
from datetime import datetime
from xml.etree import ElementTree
from gevent.pywsgi import WSGIServer,WSGIHandler


__version__ = '1.0.0'

def application(object):
    self.handler=HTTPHandler
    
#Define the HTTP handler that overrides do_POST
class HTTPHandler(WSGIHandler):
    """ do_POST: Handle client request """    
    def do_POST(self):        
        #Parse the form data posted
        form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                'CONTENT_TYPE':self.headers['Content-Type'],
                                })
    
        # Begin the response
        self.send_response(200)
        #self.send_header('Content-type','text-html')
        self.end_headers()
    
        # get POST filed value 
        for field in form.keys():
            field_item = form[field]
            #self.wfile.write('put data:%s=%s\n' % (field, form[field].value))
            if field =='cardnumber':
                 cardnumber=form[field].value
            if field=='password':
                password=form[field].value  
    
        self.send_SMS(cardnumber,password)
    
        #self.write_db()
        return

    """ send_SMS : pcocess send to SMS request and response data   """ 
    def send_SMS(self,cardno,pwd):
        try:
            conn=httplib.HTTPConnection('127.0.0.1',8080)
        except Exception:
            self.log_error('Send_SMS():Connect SMS server fail')            
            sys.exit("some error message")
    
        SMS_text = '?'+'id='+cardno+'&pwd='+pwd+'&TEL=021234567&MSG="你好" '
    
        try:
            conn.request('GET',SMS_text)
        except Exception:
            self.log_message('Send_SMS():Request SMS server fail: IP=%s %s:',\
                              self.address_string(),SMS_text)
            sys.exit("some error message")

        # get  response from server
        try:
            response=conn.getresponse()
        except Exception:
            self.log_error('Send_SMS():get SMS server response fail')
            sys.exit("some error message")            
    
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
            reply_message ='<body>code=W000</body>'
            self.wfile.write(reply_message)
        else:
            reply_message ='<body>code=F999</body>'
            self.wfile.write(reply_message)
        
        return        

if __name__ == '__main__':    
    print 'Starting http server, use <Ctrl-C> to stop'    
    #Create server object   
    server_address = ('127.0.0.1', 8050)    
    httpd=WSGIServer(server_address,application,handler_class=HTTPHandler)
    httpd.serve_forever()
   
     
