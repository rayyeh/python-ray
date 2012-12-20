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

   
   
import sys,getopt,os,time,urllib,urllib2
from collections import OrderedDict
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
            SMS_MSG ="UBEZ_server_acquirer_service_down"
        elif serverip == '192.168.110.133' and serverport == 4900:
            SMS_MSG ="UBEZ_server_issuer_service_down"
        else:
            SMS_MSG = "Service_down_IP:%s,PORT:%s"  %(str(serverip),str(serverport))
        
            
        f=open(dirname+'\message.txt','w+')
        f.write(SMS_MSG)
        f.close()
        ftp=FTP(OPHOST)
        ftp.login(OPID,OPPWD)
        fmsgname =dirname+'message.txt'
        fwavname =dirname+'sound.wav'
        ftp.retrlines('LIST')
        '''try:
            file=open(fwavname,'rb')        
            ftp.storbinary('STOR '+'sound.wav',file)
            file.close()

            file=open(fmsgname,'rb')
            ftp.delete('message.txt')
            ftp.storbinary('STOR '+'message.txt',file)
            file.close()
            
            ftp.quit()
            ftp.close()
        except Exception,err:
            print err'''
        
        for tel in TELLIST:
            if tel <> '':
                data=OrderedDict();
                data['ID']=str(ID)
                data['PWD']=str(PWD)
                data['TEL']=str(tel)
                data['MSG']='ABCDEFGHIJKLMNPQRSTUVWXYZ'
                url_values=urllib.urlencode(data)
                url='http://172.28.223.10:9080/SMSer'
                full_url=url+'?'+url_values
                print full_url
                response=urllib2.urlopen(full_url)
                data_received=response.read()        
                msg1=str(data_received)
                msg=msg1.replace("Big5","utf-8")
                print msg            
                
                '''tree=ElementTree.fromstring(str(msg))        
                for node in tree.iter():            
                    if node.tag == 'SEND-RETN-DATE' : 
                        print 'SEND-RETN-DATE:',node.text
                    if node.tag == 'SEND-RETN-CODE':
                        print 'SEND-RETN-CODE:',node.text
                    if node.tag == 'SEND-RETN-CODE-DESC':
                        print 'SEND-RETN-CODE-DESC:', node.text
                    if node.tag == 'MSG-ID':
                        print 'MSG-ID:',node.text
                '''
                #print 'Resp status:',response.status,'\tResp reason:',response.reason            
        
                time.sleep(1)
        
        
if __name__ == "__main__":
    main(sys.argv[1:])    
