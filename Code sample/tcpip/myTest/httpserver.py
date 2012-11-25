import os, sys
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import httplib
from datetime import time,datetime
import random
import gevent.monkey; gevent.monkey.patch_all()

#Define the HTTP handler that overrides do_POST
class httpServHandler(BaseHTTPRequestHandler):
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

        #send content
        #self.wfile.write('Client: %s\n' % str(self.client_address))
        #self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        #self.wfile.write('Path: %s\n' % self.path)
        #self.wfile.write('Form data:\n')

        # get form value and  send back to reponse
        for field in form.keys():
            field_item = form[field]
            self.wfile.write('%s=%s\n' % (field, form[field].value))                   
        
        self.send_SMS()
        self.wfile.write(datetime.now())
        return

    def  send_SMS(self):
        #print '*** Send to SMSsvr.....'
        conn=httplib.HTTPConnection('127.0.0.1',8080)
        SMS_text = '?'+'id='+str(random.randint(1, 1000))
        conn.request('GET',SMS_text)

        #get  response from server
        response=conn.getresponse()
        
        #print SMS response and data
        #print '*** get SMS response....'
        #print '*** response.status:', response.status,'\tresponse reason:',response.reason
        data_received=response.read()
        #print data_received
        #print '*** get SMS response end...'
        return
        

if __name__ == '__main__':
    #Set the root directory
    #os.chdir('d:/myTest')
    print 'Starting http server, use <Ctrl-C> to stop'
	
    #Create server object	
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, httpServHandler)
    print('http server is running...')
    httpd.serve_forever()
     
