import urlparse
import random
from gevent.pywsgi import WSGIServer
from flask import Flask,request
from datetime import datetime
from logging import Logger as logger

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def do_GET():
    if request.method == 'GET':
        msg0='<?xml version="1.0" encoding="Big5"?>'        
        msg1='<SEND> <TxnID>SENDMSG<SEND-RETN-DATE>'
        msg2='</SEND-RETN-DATE>\
                   <SEND-RETN-CODE>0000</SEND-RETN-CODE>\
                   <SEND-RETN-CODE-DESC>"中文"</SEND-RETN-CODE-DESC>\
</TxnID><SYSMSG><MSG-ID>'
        msg3='</MSG-ID><MSG-DESC></MSG-DESC></SYSMSG></SEND>'    
        d=datetime.now()
        msg_datetime=str(d.strftime("%Y%m%d%H%m%S"))
        msg_id=str(random.randint(1, 1000000))
        message=msg0+msg1+msg_datetime+msg2+msg_id+msg3
        return message
        
if __name__ == '__main__':
    print 'Starting http server, use <Ctrl-C> to stop' 
       
    server_address = ('127.0.0.1', 8080)
    #httpd=WSGIServer(server_address,app)
    print 'http server is running ....',server_address    
    #httpd.serve_forever()
    
    app.run('',8080,debug=True)
