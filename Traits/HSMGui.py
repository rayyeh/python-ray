# -*- coding:utf-8 -*-
"""
Created on 2010/6/23

@author: rayyeh
"""
from enthought.traits.api import Str, Date, File, Int, Directory, Bool, \
    HasTraits, Button, Any, Instance
from enthought.traits.ui.api import View, Item, Group, FileEditor, \
    DirectoryEditor, TextEditor, CheckListEditor, OKCancelButtons, Action, spring, \
    VSplit, Tabbed, VGroup, OKButton, CancelButton, HGroup, VGrid, VFlow, Tabbed
from enthought.traits.ui.file_dialog import open_file
from enthought.traits.ui.menu import MenuBar, ToolBar, Menu
import binascii
import socket
import sys


class HSM(HasTraits):
    connect_button=Button('Connect')
    disconn_button=Button('Disconect')
    EncPIN_button=Button('EncPIN(BA)')
    PINLMK2ZPK_button=Button('PINLMK2ZPK(JG)')
    genPVV_button=Button('genPVV(DG)')
    genCVV_button=Button('genCVV(CW)')
    VerifyPinVISATPK_button=Button('VerifyPinVISATPK(DC)')
    VerifyPinVISAZPK_button=Button('VerifyPinVISAZPK(EC)')
    VerifyVISACVV_button=Button('VerifyCVV(CY)')
    GenPINOffset_button=Button('GenPINoffset(EE)')
    GenRandomPIN_button=Button('GenRandomPIN(JA)')
    DecPIN_button=Button('DecPIN(NG)')
    VerifyARQC_button=Button('VerifyARQC(KQ)')
        
    ZPK =Str('U2CFDF85580B3722AD14B412CE64FDC80')
    PVK=Str('84A24A12E2A48F2484A24A12E2A48F24')
    CVK=Str('80E263751D939600DCE4774949AB4CBC')
    TPK=Str('80E263751D939600DCE4774949AB4CBC')
    MDK=Str('80E263751D939600DCE4774949AB4CBC')
    PIN_Block_LMK=Str
    PVV=Str
    PIN=Str("1234")
    pan=Str('4579520612345702')
    expire_date=Str('4902')
    CVV=Str
    Resp=Str
    PIN_Block_ZPK=Str
    PIN_Block_TPK=Str
    output=Str('-----------------  Begin   ---------------\n')
    sock=socket.socket    
    
            
    serverIP = "192.168.110.180"
    serverPort = Int(1500)
    
    view1=View(HGroup(
                    Item('serverIP'),
                    Item('serverPort'),
                    HGroup(Item('connect_button',show_label=False),
                          Item('disconn_button',show_label=False),
                          show_border=True),
                    show_border=True                    
                    ),
                VGroup(Item('ZPK',label='ZPK'),
                      Item('TPK',label='TPK'),
                      Item('MDK',label='MDK'),
                      Item('PVK',label='PVK'),
                      Item('CVK',label='CVK'),                      
                      show_border=True 
                      ),
                Group(Item('pan'),
                      Item('expire_date',label=u'Expire_date(yymm)'),
                      Item('PIN'),Item('CVV'),Item('PIN_Block_ZPK'),
                      Item('PIN_Block_TPK'),Item('PIN_Block_LMK'),          
                      orientation='vertical',columns=4,show_border=True                       
                      ),
                Tabbed(
                Group(Item('genCVV_button',show_label=False,\
                            tooltip=u'Generate a VISA CVV'),                      
                      Item('VerifyVISACVV_button',show_label=False,\
                            tooltip=u'Verify a VISA CVV'),
                      Item('VerifyARQC_button',show_label=False,\
                            tooltip=u'Verify ARQC'),                       
                      orientation='vertical', columns=4,label="CVV-ARQC"),
                 Group(Item('EncPIN_button',show_label=False,\
                            tooltip=u'Encrypt a Clear PIN'),
                       Item('DecPIN_button',show_label=False,\
                            tooltip=u'Decrypt a Encrypted PIN'),
                       Item('GenPINOffset_button',show_label=False,\
                            tooltip=u'Generate an IBM PIN Offset'),
                       Item('GenRandomPIN_button',show_label=False,\
                            tooltip=u'Generate a Random PIN'),
                       Item('genPVV_button',show_label=False,\
                            tooltip=u'Generate a VISA PVV'),
                       Item('PINLMK2ZPK_button',show_label=False,\
                            tooltip=u'Translate a PIN from LMK to ZPK Encryption'),                       
                       Item('VerifyPinVISATPK_button',show_label=False,\
                            tooltip=u'Verify a Terminal PIN Using the VISA Method'),
                       Item('VerifyPinVISAZPK_button',show_label=False,\
                            tooltip=u'Verify an Interchange PIN Using the VISA Method'), 
                       orientation='vertical',columns=4,label="PIN",
                       show_border=True),
                       ),              
                 Item('output',editor=TextEditor(auto_set=True),style='custom'),
                 title = "HSMGui.py",
                 kind='live',
                 buttons=[OKButton,CancelButton],
                 width=900,height=700,
                 resizable =True
            )         
    

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
    
    def _testconnect(self):
        if not isinstance(self.sock,socket.socket): 
            self.output='%sPlease connect HSM First\n' %(self.output)
            return False
        
        else :
            return True
                
    def _EncPIN_button_changed(self): 
             
        if self.PIN == '':
            self.output = 'Pin Value is null\n'
        elif self._testconnect():        
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
        
            self.sock.send(message)
            BAresp=self.sock.recv(1024)
            self.PIN_Block_LMK=BAresp[10:]
            print 'PIN_Block_LMK->',self.PIN_Block_LMK
            self.output='%sPIN_Block_LMK:%s\n' %(self.output,self.PIN_Block_LMK)
            return self.PIN_Block_LMK
            
    def _DecPIN_button_changed(self):
        if self._testconnect():
            if self.PIN_Block_LMK == ''  and self.PIN =='':
                self.output='Generate LMK_PIN first,Execute BA button\n'
            else:    
                """Decrypt PIN  """
                msg_header ='0001'
                command_code ='NG'
                
                data =msg_header+command_code+self.pan[2:16]+self.PIN_Block_LMK    
                x=str(hex(len(data)))
                x.split('x')
                z=str(x[2:])
                message_len=binascii.a2b_hex(z.zfill(4))
                message=message_len+data
                self.sock.send(message)
                NGresp=self.sock.recv(1024)
                PIN=NGresp[5:12]
                self.output='%sClear PIN:%s\n' %(self.output,self.PIN)             
    
    def _PINLMK2ZPK_button_changed(self):
        if self._testconnect():
            """  Translate a PIN from LMK to ZPK Encryption """
            msg_header ='0001'
            command_code ='JG'
            pin_block_format ='01'
            pan_data =self.pan[3:15]
            data =msg_header+command_code+self.ZPK+pin_block_format+pan_data+self.PIN_Block_LMK

            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            self.sock.send(message)
            self.Resp=self.sock.recv(1024)
            self.PIN_Block_ZPK=self.Resp[10:]
            self.output='%sPIN_Block_ZPK:%s\n' %(self.output,self.PIN_Block_ZPK)
            
            msg_header ='0001'
            command_code ='JG'
            pin_block_format ='01'
            pan_data =self.pan[3:15]
            data =msg_header+command_code+self.TPK+pin_block_format+pan_data+self.PIN_Block_LMK

            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            self.sock.send(message)
            self.Resp=self.sock.recv(1024)
            self.PIN_Block_TPK=self.Resp[10:]
            self.output='%sPIN_Block_TPK:%s\n' %(self.output,self.PIN_Block_TPK)


    def _genPVV_button_changed(self):
        if self._testconnect():
            self.PIN_Block_LMK=self._EncPIN_button_changed()
            """ Generate a VISA PIN Verification Value"""
            msg_header ='0001'
            command_code ='DG'
            pvki='1'
            pan_data =self.pan[3:15]
            data =msg_header+command_code+self.PVK+self.PIN_Block_LMK+pan_data+ pvki
    
            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            self.sock.send(message)
            DGresp=self.sock.recv(1024)
            self.PVV=DGresp[10:]
            print  'PVV ->',self.PVV
            self.output='%sPVV:%s\n' %(self.output,self.PVV)

    def _genCVV_button_changed(self):
        if self._testconnect():
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
            CWresp=self.sock.recv(1024)
            CVV=CWresp[10:13]
            self.output='%sService-Code:%s\t CVV:%s\n' %(self.output,service1,CVV)
    
            data =msg_header+command_code+self.CVK+self.pan+';'+self.expire_date+service2
            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            print message
            self.sock.send(message)
            CWresp=self.sock.recv(1024)
            CVV=CWresp[10:13]
            self.output='%sService-Code:%s\t CVV:%s\n' %(self.output,service2,CVV)

    def _VerifyVISACVV_button_changed(self):
        if self._testconnect():
            """Decrypt PIN  """
            msg_header ='0001'
            command_code ='CY'
                
            data =msg_header+command_code+self.CVK+self.CVV+self.pan+";"+self.expire_date+"201"    
            x=str(hex(len(data)))
            x.split('x')                
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data                
            self.sock.send(message)
            self.Resp=self.sock.recv(1024)
            self.output='%sVerifyVISACVV reponse: %s \n' %(self.output,self.Resp[2:10])
        
    def _VerifyPinVISATPK_button_changed(self):
        if self._testconnect():
            """VerifyPinVISATPK """
            msg_header ='0001'
            command_code ='DC'
            
            data =msg_header+command_code+self.TPK+self.PVK+self.PIN_Block_TPK+"01"+\
                  self.pan[3:15]+'1'+self.PVV
    
            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            self.sock.send(message)
            
            #print 'Generate a VISA CVV IN->',binascii.b2a_hex(message)
            self.Resp=self.sock.recv(1024)
            self.output='%s Verify a Terminal PIN Using the VISA mehtod:%sn' %(self.output,self.Resp[3:20])
            
    def _VerifyPinVISAZPK_button_changed(self):
        if self._testconnect():
            """VerifyPinVISAZPK """
            msg_header ='0001'
            command_code ='EC'
            
            data =msg_header+command_code+self.ZPK+self.PVK+self.PIN_Block_ZPK+"01"+\
                  self.pan[3:15]+'1'+self.PVV
    
            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            self.sock.send(message)
            
            #print 'Generate a VISA CVV IN->',binascii.b2a_hex(message)
            self.Resp=self.sock.recv(1024)
            self.output='%s Verify an Interchange PIN Using the VISA mehtod:%sn' %(self.output,self.Resp[3:20])
      
        
                   
    def _GenPINOffset_button_changed(self):
        self.output ='Wait for build\n'
        
    def _GenRandomPIN_button_changed(self):
        if self._testconnect():
            """GenRandomPIN """
            msg_header ='0001'
            command_code ='JA'
            
            data =msg_header+command_code+self.pan[3:15]+'04'
    
            x=str(hex(len(data)))
            x.split('x')
            z=str(x[2:])
            message_len=binascii.a2b_hex(z.zfill(4))
            message=message_len+data
            self.sock.send(message)
            
            self.Resp=self.sock.recv(1024)
            self.PIN=self.Resp[10:14]
            self.output='%sGenerate Random PIN,return-code:%s,PIN value:%s\n' \
             %(self.output,self.Resp[8:10],self.PIN)
            
       
    def _VerifyARQC_bytton_change(self):
    	#self.output ='Wait for build\n'
        print ""
        

if __name__ == '__main__':
    hsm=HSM()
    #hsm.configure_traits()
    hsm.configure_traits(view='view1')
    
