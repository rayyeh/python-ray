# -*-  coding :UTF-8  -*-

import sys
import cgi
import httplib
import random
import logging
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from xml.etree import ElementTree

#import gevent.monkey; gevent.monkey.patch_all()


#Define the HTTP handler that overrides do_POST
class httpServHandler(BaseHTTPRequestHandler):
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)

    def do_POST(self):
        #Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
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
            self.wfile.write('put data:%s=%s\n' % (field, form[field].value))

        self.send_SMS()
        reply_message = '<body>code=W000</body>'
        self.wfile.write(reply_message)
        return

    def send_SMS(self):
        try:
            conn = httplib.HTTPConnection('127.0.0.1', 8080)
        except Exception:
            logging.error('connect SMS server fail')

        SMS_text = '?' + 'id=' + str(random.randint(1, 1000))
        try:
            conn.request('GET', SMS_text)
        except Exception:
            logging.error('request SMS server fail:')
            sys.exit("some error message")

        #get  response from server
        try:
            response = conn.getresponse()
        except Exception:
            logging.error('get SMS server response fail')
            sys.exit("some error message")


        #print '*** response.status:', response.status,'\tresponse reason:',response.reason
        data_received = response.read()
        msg = data_received.replace("Big5", "utf-8")
        tree = ElementTree.fromstring(msg)

        for node in tree.iter():
            self.wfile.write('%s=%s\n' % (node.tag, node.text))
        return


if __name__ == '__main__':
    #Set the root directory

    print 'Starting http server, use <Ctrl-C> to stop'

    #Create server object   
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, httpServHandler)
    print('http server is running...')
    httpd.serve_forever()
     
