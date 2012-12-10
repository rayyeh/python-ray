#-*- coding:utf-8 -*-

__author__ = "Ray Yeh"
__version__ = "1.0"
__date__ = "$Date: 2012/12/05$"
__copyright__ = "Copyright (c) 2012 Ray Yeh"
__license__ = "Python"

import sys,getopt,os,time
from socket import *
from httplib import HTTPConnection         
from xml.etree import ElementTree
from ConfigParser import SafeConfigParser
import logging
from logging.handlers import RotatingFileHandler
import module_locator

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
    #dirname=os.path.dirname(os.path.abspath(__file__))    
    path=dirname.replace('\\','/')
        
    config = SafeConfigParser()
    config.read(path+('/ubez.ini'))  
    ID=config.get('sms','id')
    PWD=config.get('sms','pwd')
    SMSHOST=config.get('sms','smshost')
    SMSPORT=config.getint('sms','smsport')
    SMSTIMER=config.getint('sms','smstimer')
    TEL=config.get('sms','tel')
    TRYLIMIT=config.getint('sms','trylimit')
    WAITTIME=config.getint('sms','waittime')
    
    logger = logging.getLogger(config.get('sms','logname'))
    formatter = logging.Formatter\
        ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')    
    file_handler = RotatingFileHandler((dirname+'\ubez.log'), 'a', 4096, 5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
            
    serverip=''
    serverport= 4500
    try:
        opts, args = getopt.getopt(argv,"hi:p:",["ip=","port="])
    except getopt.GetoptError:
        print 'Usage:ubez.py -i <ipaddress> -p <portnumber>'
        sys.exit(2)    
    
    if len(opts) <> 2: 
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
             
    
    for i in range(1,TRYLIMIT+1):
        LOSTCONNECT=False    
        sSock = socket(AF_INET, SOCK_STREAM)   
        try: 
            #Connect to server
            sSock.connect((serverip, serverport))
        except :
            LOSTCONNECT=True
            msg='Try %s time Connect IP: %s Port: %s  fail' %(str(i),serverip,str(serverport))
            print msg
            logger.error(msg)         
        else:
            msg='Try %s time Connect IP: %s Port: %s OK' %(str(i),serverip,str(serverport))
            print msg
            logger.error(msg)  
        finally:        
            sSock.close()
        time.sleep(3)
        
    if LOSTCONNECT:
        try:
            conn=HTTPConnection(SMSHOST,SMSPORT)
        except Exception as err:
            msg='Connect SMS fail: %s' % str(err)
            print msg
            logger.error(msg) 
            sys.exit(2)
        
        if serverport == 4500 or serverport == 4700:
            SMS_MSG ='UBEZ server acquirer service down'
        elif serverport == 4900:
            SMS_MSG ='UBEZ server issuer service down'
        else:
            SMS_MSG = 'service down ip:'+str(serverip)+' port:'+str(serverport)
            
        SMS_text = '?'+'id='+ID+'&pwd='+PWD+'&TEL='+TEL+'&MSG='+SMS_MSG
        #print SMS_text
        
        try:
            conn.request('GET',SMS_text)
        except Exception as err:            
            msg='Send request to SMS server fail: %s ' %str(err)
            print msg
            logger.error(msg) 
            sys.exit(2)
        
        #get  response from server
        try:
            response=conn.getresponse()
        except Exception as err:
            msg='Can not get response :%s ' %(str(err))
            print msg
            logger.error(msg) 
            sys.exit(2)
            
        #print 'Resp status:',response.status,'\tResp reason:',response.reason            
        
if __name__ == "__main__":
    main(sys.argv[1:])    
