__author__ = "Ray Yeh"
__version__ = "1.1"
__date__ = "$Date: 2012/12/05$"
__copyright__ = "Copyright (c) 2012 Ray Yeh"
__license__ = "Python"

'''
   The program detect tcpip client connection and send
   message to IBM Command console.
   configuration file = ubez.ini
   Usage : ubezibm -i ip  -p port
'''

import sys
import getopt
import time
import urllib
import urllib2
from datetime import datetime
import module_locator
from collections import OrderedDict
from socket import *
from ConfigParser import SafeConfigParser
import logging
from logging.handlers import RotatingFileHandler
from ftplib import FTP


def main(argv):
    """UBEZ connection test program
    Usage: python ubez.py [ip] [port]
    Options:
      -i ..., --ip=...   ip addresss
      -h, --help         show this help
      -p                 port number
    """
    #print 'ARGV      :', sys.argv
    dirname = module_locator.module_path()
    #dirname = os.path.dirname(os.path.abspath(__file__))
    path = dirname.replace('\\', '/')

    config = SafeConfigParser()
    config.read(path + ('/ubez.ini'))

    #SMS id/password    
    ID = config.get('SMS', 'id')
    PWD = config.get('SMS', 'pwd')
    SMSURL = config.get('SMS', 'smsurl')

    TELLIST = []
    TELLIST.append(config.get('ONCALL', 'tel1'))
    TELLIST.append(config.get('ONCALL', 'tel2'))
    TELLIST.append(config.get('ONCALL', 'tel3'))
    TELLIST.append(config.get('ONCALL', 'tel4'))
    TELLIST.append(config.get('ONCALL', 'tel5'))

    TRYLIMIT = config.getint('SYSTEM', 'trylimit')
    WAITTIME = config.getint('SYSTEM', 'waittime')

    OPHOST = config.get('IBM', 'ophost')
    OPID = config.get('IBM', 'opid')
    OPPWD = config.get('IBM', 'oppwd')

    IBMFTP = config.getint('SYSTEM', 'IBMFTP')
    SMS = config.getint('SYSTEM', 'SMS')
    
    #SMS reciver name 
    DESTNAME = config.get('SYSTEM','destname')

    logger = logging.getLogger(config.get('SYSTEM', 'logname'))
    formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler((dirname + '\ubez.log'), 'a', 81920, 10)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    serverip = ''
    serverport = 4500
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["ip=", "port="])
    except getopt.GetoptError:
        print 'Usage:ubez.py -i <ipaddress> -p <portnumber>'
        sys.exit(2)

    if len(opts) != 2:
        print 'Usage:ubez.py -i <ipaddress> -p <portnumber>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'ubez.py -i <ipaddress> -p <portnumber>'
            sys.exit()
        elif opt in ("-i", "--ip"):
            serverip = arg
        elif opt in ("-p", "--port"):
            serverport = int(arg)

    msg = '-------------- Begin log -------------------'
    logger.warning(msg)
    for i in range(1, TRYLIMIT + 1):
        LOSTCONNECT = False
        sSock = socket(AF_INET, SOCK_STREAM)
        try:
            #Connect to server
            sSock.connect((serverip, serverport))
        except Exception, err:
            LOSTCONNECT = True
            msg = 'Try %s time Connect IP: %s Port: %s  fail,Except: %s' \
                 % (str(i), serverip, str(serverport), str(err))
            print msg
            logger.error(msg)
        else:
            msg = 'Try %s time Connect IP: %s Port: %s OK' \
                    % (str(i), serverip, str(serverport))
            print msg
            logger.error(msg)
        finally:
            sSock.close()
        time.sleep(WAITTIME)

    if LOSTCONNECT:
        SMS_MSG = "Service:%s,IP:%s,PORT:%s_is_Down,%s" \
                    % (str(DESTNAME),str(serverip), str(serverport), str(datetime.now()))
        FTP_MSG = "Service:%s,IP:%s,PORT:%s_is_Down,%s,call COSES 0963336528" \
                    % (str(DESTNAME),str(serverip), str(serverport), str(datetime.now()))

        print SMS_MSG
        print FTP_MSG
        #FTP to IBM Command console
        if IBMFTP is 1:
            #print 'use IBMFTP function'
            f = open(dirname + '\message.txt', 'w+')
            f.write(FTP_MSG)
            f.close()
            try:
                ftp = FTP(OPHOST)
                ftp.login(OPID, OPPWD)
                fmsgname = dirname + '\message.txt'
                fwavname = dirname + '\sound.wav'
                ftp.retrlines('LIST')

                filename = open(fwavname, 'rb')
                ftp.storbinary('STOR ' + 'sound.wav', filename)
                filename.close()

                filename = open(fmsgname, 'rb')
                #ftp.delete('message.txt')
                ftp.storbinary('STOR ' + 'message.txt', filename)
                filename.close()

                ftp.quit()
                ftp.close()
            except Exception, err:
                print logger.error(err)

        # Send SMS message to SMS server
        if SMS is 1:
            #print 'use SMS function'
            for tel in TELLIST:
                if tel != '':
                    data = OrderedDict()
                    data['username'] = str(ID)
                    data['password'] = str(PWD)
                    data['dstaddr'] = str(tel)
                    data['DestName'] = DESTNAME
                    data['dlvtime'] = 0
                    data['vldtime'] = 60
                    #data['smbody']=SMS_MSG.encode('hex')
                    data['smbody'] = SMS_MSG

                    url_values = urllib.urlencode(data)

                    url = SMSURL
                    full_url = url + '?' + url_values
                    print '--------- request ----------- \n', full_url

                    try:
                        response = urllib2.urlopen(full_url)
                        data_received = response.read()
                        msg1 = str(data_received)
                        print '--------- reponse -----------\n', msg1
                        logger.error(msg1)
                    except Exception, err:
                        errmsg = str(err) + ':' + SMSURL
                        logger.error(errmsg)
                    finally:
                        time.sleep(1)


if __name__ == "__main__":
    main(sys.argv[1:])
