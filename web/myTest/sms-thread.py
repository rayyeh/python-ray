from future import standard_library
standard_library.install_aliases()
from builtins import str
# -*-  coding :UTF-8  -*-

from http.server import BaseHTTPRequestHandler
import urllib.parse
from datetime import datetime
import random
from socketserver import ThreadingMixIn
#import gevent.monkey; gevent.monkey.patch_all()

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        message_parts = [
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                                        self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            #'SERVER VALUES:',
            #'server_version=%s' % self.server_version,
            #'sys_version=%s' % self.sys_version,
            #'protocol_version=%s' % self.protocol_version,
            #'',
            #'HEADERS RECEIVED:',
        ]

        self.send_response(200)
        self.end_headers()

        msg1 = '<SEND> <TxnID>SENDMSG<SEND-RETN-DATE>'
        msg2 = '</SEND-RETN-DATE>\
                   <SEND-RETN-CODE>0000</SEND-RETN-CODE>\
                   <SEND-RETN-CODE-DESC>Sucess</SEND-RETN-CODE-DESC>\
                    </TxnID><SYSMSG><MSG-ID>'
        msg3 = '</MSG-ID><MSG-DESC></MSG-DESC></SYSMSG></SEND>'
        d = datetime.now()
        msg_datetime = str(d.strftime("%Y%m%d%H%m%S"))
        msg_id = str(random.randint(1, 1000000))
        message = msg1 + msg_datetime + msg2 + msg_id + msg3
        self.wfile.write(message)
        return


if __name__ == '__main__':
    from http.server import HTTPServer

    class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
        pass

    server = ThreadingHTTPServer(('localhost', 8080), GetHandler)
    print 'Starting SMS server, use <Ctrl-C> to stop'
    server.serve_forever()
