# -*- coding:utf-8 -*-
"""
Created on 2010/6/23

@author: rayyeh
"""
import socket
import sys
import binascii
from enthought.traits.api import Str,Date,File,Int,Directory,Bool,\
    HasTraits,Button,Any,Instance
from enthought.traits.ui.api import View,Item,Group,FileEditor,DirectoryEditor,\
    TextEditor,CheckListEditor,OKCancelButtons,Action,spring,VSplit,Tabbed,VGroup,\
    OKButton,CancelButton,HGroup
from enthought.traits.ui.menu import MenuBar,ToolBar,Menu
from enthought.traits.ui.file_dialog import open_file


class HSM(HasTraits):
    connect_button=Button('Connect')
    disconn_button=Button('Disconect')
    EncPIN_button=Button('EncPIN')
    PINLMK2ZPK_button=Button('PINLMK2ZPK')
    genPVV_button=Button('genPVV')
    genCVV_button=Button('genCVV')
        
    ZPK =Str('U2CFDF85580B3722AD14B412CE64FDC80')
    PVK=Str('84A24A12E2A48F2484A24A12E2A48F24')
    CVK=Str('80E263751D939600DCE4774949AB4CBC')
    PIN_LMK=Str
    PVV=Str
    PIN=Str("1234")
    pan=Str('4579520612345702')
    expire_date=Str('4902')
    output=Str('-----------------  Begin   ---------------\n')
    sock=socket.socket    
    
            
    serverIP = "192.168.110.180"
    serverPort = Int(1500)
    
    view1=View(HGroup(
                    Item('serverIP'),
                    Item('serverPort'),
                    VGroup(Item('connect_button',show_label=False),
                          Item('disconn_button',show_label=False),
                          show_border=True 
                        ),
                    show_border=True                    
                    ),
                Group(Item('ZPK',label='ZPK'),
                      Item('PVK',label='PVK'),
                      Item('CVK',label='CVK'),
                      show_border=True 
                      ),
                Group(Item('pan'),
                      Item('expire_date',label=u'Expire_date(yymm)'),
                      Item('PIN'),                      
                      show_border=True                       
                      ),
                HGroup(Item('EncPIN_button',show_label=False,\
                            tooltip=u'用 LMK 加密 PIN'),
                       #spring,
                       Item('PINLMK2ZPK_button',show_label=False,\
                            tooltip=u'用 ZPK 加密 PIN'),
                       #spring,
                       Item('genPVV_button',show_label=False,\
                            tooltip=u'產生 PVV'),
                       #spring,
                       Item('genCVV_button',show_label=False,\
                            tooltip=u'產生 CVV'),
                       show_border=True
                       ),              
                 Item('output',editor=TextEditor(auto_set=True),style='custom'),
                 title = "HSMGui.py",
                 kind='live',
                 buttons=[OKButton,CancelButton],
                 width=800,height=600,
                 resizable =True
            )         
    
    #def _anytrait_changed(self,name,old,new):
    #    print 'object %s changed from  %s to %s ' %(name,old,new)        
        
    def _connect_button_changed(self):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error, e:
            print  'socket error:',e
            self.output='socket error:',e
            self.sock = None

        try:
            self.output='%sConnecting... %s\n' %(self.output,self.serverIP) 
            print 'Connecting..%s\n' %(self.serverIP)
            print ' serverip:%s serverport %s'%(type(self.serverIP)\
                      ,type(self.serverPort))
                      
            self.sock.connect((self.serverIP, self.serverPort))
            print 'Connected-> %s\n' %(self.serverIP)
            self.output= '%sConnected-> %s\n' %(self.output,self.serverIP)
            
        except socket.error:
            self.sock.close()
            self.sock = None

        if self.sock is None:
            print  'Could not connect' 
            self.output='%sCould not connect.\n' %(self.output)
            
    def _disconn_button_changed(self):
        print 'Closing ....',self.serverIP
        self.sock.close()
        self.output='%sClosing-> %s\n' %(self.output,self.serverIP)
        
    def _EncPIN_button_changed(self):              
        #self.output ='%sEncrypt a Clear PIN\n'%(self.output)
        
        if not isinstance(self.sock,socket.socket): 
            self.output='%sPlease connect HSM First' %(self.output)
        else:
            msg_header ='0001'
            command_code ='BA'
            pin_data=self.PIN+'F'
            pan_data =self.pan[3:15]
            data =msg_header+command_code+pin_data+pan_data
            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
        
            #print 'Encrypt Clear PIN IN->',binascii.b2a_hex(message)              
            self.sock.send(message)
            BAresp=self.sock.recv(1024)
            self.PIN_LMK=BAresp[10:]
            #print 'Encrypt Clear PIN OUT ->',BAresp
            print 'PIN_LMK->',self.PIN_LMK
            self.output='%sPIN_LMK:%s\n' %(self.output,self.PIN_LMK)
            return self.PIN_LMK
            

    def _PINLMK2ZPK_button_changed(self):
        """  Translate a PIN from LMK to ZPK Encryption """
        msg_header ='0001'
        command_code ='JG'
        pin_block_format ='01'
        pan_data =self.pan[3:15]
        data =msg_header+command_code+self.ZPK+pin_block_format+pan_data+self.PIN_LMK

        x=str(hex(len(data)))
        x.split('x')
        z=str(x[2:])
        message_len=binascii.a2b_hex(z.zfill(4))
        message=message_len+data
        #print 'Translate a PIN from LMK to ZPK Encryption IN->',binascii.b2a_hex(message)
        self.sock.send(message)
        JGresp=self.sock.recv(1024)
        PIN_BLOCK_ZPK=JGresp[10:]
        #print 'Translate a PIN from LMK to ZPK Encryption OUT->',JGresp
        print 'PIN_BLOCK-ZPK->',PIN_BLOCK_ZPK
        self.output='%sPIN_BLOCK-ZPK:%s\n' %(self.output,PIN_BLOCK_ZPK)


    def _genPVV_button_changed(self):
        self.PIN_LMK=self._EncPIN_button_changed()
        """ Generate a VISA PIN Verification Value"""
        msg_header ='0001'
        command_code ='DG'
        pvki='1'
        pan_data =self.pan[3:15]
        data =msg_header+command_code+self.PVK+self.PIN_LMK+pan_data+ pvki

        x=str(hex(len(data)))
        x.split('x')
        z=str(x[2:])
        message_len=binascii.a2b_hex(z.zfill(4))
        message=message_len+data
        self.sock.send(message)
        #print 'Generate a VISA PVV IN->',binascii.b2a_hex(message)
        DGresp=self.sock.recv(1024)
        self.PVV=DGresp[10:]
        #print 'Generate a VISA PVV OUT->',DGresp
        print  'PVV ->',self.PVV
        self.output='%sPVV:%s\n' %(self.output,self.PVV)


    def _genCVV_button_changed(self):
        """Generate a VISA CVV """
        msg_header ='0001'
        command_code ='CW'
        service1='201'
        service2='000'
        data =msg_header+command_code+self.CVK+self.pan+';'+self.expire_date+service1

        x=str(hex(len(data)))
        x.split('x')
        z=str(x[2:])
        message_len=binascii.a2b_hex(z.zfill(4))
        message=message_len+data
        self.sock.send(message)
        #print 'Generate a VISA CVV IN->',binascii.b2a_hex(message)
        CWresp=self.sock.recv(1024)
        CVV=CWresp[10:13]
        #print 'Generate a VISA CVV OUT->',CWresp
        self.output='%sService-Code:%s\t CVV:%s\n' %(self.output,service1,CVV)
        print  'Service-Code->',service1,'\t CVV->',CVV

        data =msg_header+command_code+self.CVK+self.pan+';'+self.expire_date+service2
        x=str(hex(len(data)))
        x.split('x')
        z=str(x[2:])
        message_len=binascii.a2b_hex(z.zfill(4))
        message=message_len+data
        self.sock.send(message)
        CWresp=self.sock.recv(1024)
        CVV=CWresp[10:13]
        #print 'Generate a VISA CVV OUT->',CWresp
        print  'Service-Code->',service2,'\t CVV->',CVV
        self.output='%sService-Code:%s\t CVV:%s\n' %(self.output,service2,CVV)

if __name__ == '__main__':
    hsm=HSM()
    #hsm.configure_traits()
    hsm.configure_traits(view='view1')
    