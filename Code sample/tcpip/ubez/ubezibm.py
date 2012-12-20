#-*- coding:utf-8 -*-

__author__ = "Ray Yeh"
__version__ = "1.0"
__date__ = "$Date: 2012/12/05$"
__copyright__ = "Copyright (c) 2012 Ray Yeh"
__license__ = "Python"

'''
   The program detect tcpip client connection and send
   message to IBM Command console.
   configuration file = ubez.ini   
   Usage : ubezibm -i ip  -p port
'''   
   
import sys,getopt,os,time
from socket import *
from httplib import HTTPConnection
#import httplib 
from xml.etree import ElementTree
from ConfigParser import SafeConfigParser
import logging
from logging.handlers import RotatingFileHandler
import module_locator
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
    #dirname=os.path.dirname(os.path.abspath(__file__))    
    path=dirname.replace('\\','/')
        
    config = SafeConfigParser()
    config.read(path+('/ubez.ini'))  
    ID=config.get('sms','id')
    PWD=config.get('sms','pwd')
    SMSHOST=config.get('sms','smshost')
    SMSPORT=config.getint('sms','smsport')
    SMSTIMER=config.getint('sms','smstimer')
    
    TELLIST=[]
    TELLIST.append(config.get('sms','tel1'))
    TELLIST.append(config.get('sms','tel2'))
    TELLIST.append(config.get('sms','tel3'))
    TELLIST.append(config.get('sms','tel4'))
    TELLIST.append(config.get('sms','tel5'))      
    
    TRYLIMIT=config.getint('sms','trylimit')
    WAITTIME=config.getint('sms','waittime')
    
    OPHOST=config.get('sms','ophost')
    OPID=config.get('sms','opid')
    OPPWD=config.get('sms','oppwd')
    
    logger = logging.getLogger(config.get('sms','logname'))
    formatter = logging.Formatter\
        ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')    
    file_handler = RotatingFileHandler((dirname+'\ubez.log'), 'a', 4096, 5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
            
    serverip=''
    serverport= 4500
    
    # get ip-address and port number from command line
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
             
    # send to SMS server function
    def send_SMS(SMS_text):
            try:
                conn.request('GET',SMS_text)                        
            except Exception as err:            
                msg='Send request to SMS server fail: %s ' %str(err)
                logger.error(msg)
                return  
                
            #get  response from server
            try:
                response=conn.getresponse()                            
            except Exception as err:
                msg='Can not get response :%s ' %(str(err))
                logger.error(msg) 
                return          
            
            #print 'Resp status:',response.status,'\tResp reason:',response.reason            
        
            
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
        time.sleep(WAITTIME)
        
    if LOSTCONNECT:
        try:
            conn=HTTPConnection(SMSHOST,SMSPORT)            
        except Exception as err:
            msg='Connect SMS fail: %s' % str(err)
            print msg
            logger.error(msg) 
            sys.exit(2)
        
        if serverip == '192.168.110.133' and \
            (serverport == 4500 or serverport == 4700):
            SMS_MSG ="UBEZ_server_acquirer_service_down,call COSES 0963-336528"
        elif serverip == '192.168.110.133' and serverport == 4900:
            SMS_MSG ="UBEZ_server_issuer_service_down,call COSES 0963-336528"
        else:
            SMS_MSG = "Service_down_IP:%s,PORT:%s"  %(str(serverip),str(serverport))
        
            
        #send to IBM Console 
        f=open(dirname+'\message.txt','w+')
        f.write(SMS_MSG)                
        f.close()
        fmsgname =dirname+'\message.txt'
        fwavname =dirname+'\sound.wav'              
        
        ftp=FTP(OPHOST)
        ftp.login(OPID,OPPWD)
        try:
            file=open(fwavname,'rb')
            print 'sending sound.wav ... '        
            ftp.storbinary('STOR '+'sound.wav',file)
            file.close()

            file=open(fmsgname,'rb')
            ftp.delete('message.txt')
            print 'sending message.txt ...'
            ftp.storbinary('STOR '+'message.txt',file)
            file.close()
            
            ftp.quit()
            ftp.close()
        except Exception,err:
            print err        
        
        
if __name__ == "__main__":
    main(sys.argv[1:])    
