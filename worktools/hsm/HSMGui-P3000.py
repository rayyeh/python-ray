# -*- coding:utf-8 -*-
"""
Created on 2010/6/23

@author: rayyeh
"""
from builtins import str
from builtins import hex
import binascii
import socket
import sys

from enthought.traits.api import Str, Date, File, Int, Directory, Bool, \
    HasTraits, Button, Any, Instance
from enthought.traits.ui.api import View, Item, Group, FileEditor, \
    DirectoryEditor, TextEditor, CheckListEditor, OKCancelButtons, Action, spring, \
    VSplit, Tabbed, VGroup, OKButton, CancelButton, HGroup, VGrid, VFlow, Tabbed
from enthought.traits.ui.file_dialog import open_file
from enthought.traits.ui.menu import MenuBar, ToolBar, Menu


DEBUG_ON = 1


class HSM(HasTraits):
    connect_button = Button('Connect')
    disconn_button = Button('Disconect')
    EncPIN_button = Button('EncPIN(BA)')
    PINLMK2ZPK_button = Button('PINLMK2ZPK(JG)')
    genPVV_button = Button('genPVV(DG)')
    genCVV_button = Button('genCVV(CW)')
    VerifyPinVISATPK_button = Button('VerifyPinVISATPK(DC)')
    VerifyPinVISAZPK_button = Button('VerifyPinVISAZPK(EC)')
    VerifyVISACVV_button = Button('VerifyCVV(CY)')
    ZPKZMK2LMK_button = Button('ZPKZMK2LMK(FA)')
    GenPINOffset_button = Button('GenPINoffset(EE)')
    GenRandomPIN_button = Button('GenRandomPIN(JA)')
    DecPIN_button = Button('DecPIN(NG)')
    VerifyARQC_button = Button('VerifyARQC(KQ)')

    ZMK = Str('UC77A58BAD7EE39E2FAC5AE02A2A7DB2E')
    ZPK = Str('U914FCB221A02829D914FCB221A02829D')
    ZPK_ZMK = Str('U9DB32983809C188C9DB32983809C188C')
    PVK = Str('3B3A0EC90E9C558B3B3A0EC90E9C558B')
    CVK = Str('29A34CB42019217B4D7487DE72C779AD')
    # TPK=Str('80E263751D939600DCE4774949AB4CBC')
    MDK = Str('E13E5401893A1421E13E5401893A1421')
    PVKX = Str('3B3A0EC90E9C558B')

    ENC_PIN = Str
    PVV = Str
    PIN = Str("1234")
    pan = Str('4579520612345702')
    expire_date = Str('4902')
    CVV = Str
    Resp = Str
    PIN_Block_ZPK = Str
    PIN_Block_TPK = Str

    output = Str('-----------------  Begin   ---------------\n')
    sock = socket.socket

    serverIP = "192.168.10.70"
    serverPort = Int(3501)

    view1 = View(HGroup(
        Item('serverIP'),
        Item('serverPort'),
        HGroup(Item('connect_button', show_label=False),
               Item('disconn_button', show_label=False),
               show_border=True),
        show_border=True
    ),
                 Group(Item('ZMK', label='ZMK'),
                       Item('ZPK', label='ZPK_LMK'),
                       Item('ZPK_ZMK', label='ZPK_ZMK'),
                       #Item('TPK',label='TPK'),
                       Item('MDK', label='MDK'),
                       Item('PVK', label='PVK'),
                       Item('PVKX', label='PVKX'),
                       Item('CVK', label='CVK'),
                       orientation='vertical', columns=2, show_border=True
                 ),
                 Group(Item('pan'),
                       Item('expire_date', label=u'Expire_date(yymm)'),
                       Item('PIN'),
                       Item('CVV'), Item('PIN_Block_ZPK'),
                       #Item('PIN_Block_TPK'),
                       Item('ENC_PIN'),
                       Item('PVV'),
                       orientation='vertical', columns=4, show_border=True
                 ),
                 Tabbed(
                     Group(Item('genCVV_button', show_label=False, \
                                tooltip=u'Generate a VISA CVV'),
                           Item('VerifyVISACVV_button', show_label=False, \
                                tooltip=u'Verify a VISA CVV'),
                           Item('VerifyARQC_button', show_label=False, \
                                tooltip=u'Verify ARQC'),
                           orientation='vertical', columns=4, label="CVV-ARQC"),
                     Group(Item('EncPIN_button', show_label=False, \
                                tooltip=u'Encrypt a Clear PIN'),
                           Item('DecPIN_button', show_label=False, \
                                tooltip=u'Decrypt a Encrypted PIN'),
                           Item('GenPINOffset_button', show_label=False, \
                                tooltip=u'Generate an IBM PIN Offset'),
                           Item('GenRandomPIN_button', show_label=False, \
                                tooltip=u'Generate a Random PIN'),
                           Item('genPVV_button', show_label=False, \
                                tooltip=u'Generate a VISA PVV'),
                           Item('PINLMK2ZPK_button', show_label=False, \
                                tooltip=u'Translate a PIN from LMK to ZPK Encryption'),
                           #Item('VerifyPinVISATPK_button',show_label=False,\
                           #     tooltip=u'Verify a Terminal PIN Using the VISA Method'),
                           Item('VerifyPinVISAZPK_button', show_label=False, \
                                tooltip=u'Verify an Interchange PIN Using the VISA Method'),
                           Item('ZPKZMK2LMK_button', show_label=False, \
                                tooltip=u'Translate a ZPK from ZMK to LMK Encryption'),
                           orientation='vertical', columns=4, label="PIN",
                           show_border=True),
                 ),
                 Item('output', editor=TextEditor(), style='custom'),
                 title="HSMGuip3000.py",
                 kind='live',
                 buttons=[OKButton, CancelButton],
                 width=900, height=700,
                 resizable=True
    )


    def _connect_button_changed(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, e:
            print  'socket error:', e
            self.output = 'socket error:', e
            self.sock = None

        try:
            self.output = '%sConnecting... %s\n' % (self.output, self.serverIP)
            print 'Connecting..%s\n' % (self.serverIP)
            print ' serverip:%s serverport %s' % (type(self.serverIP) \
                                                      , type(self.serverPort))

            self.sock.connect((self.serverIP, self.serverPort))
            print 'Connected-> %s\n' % (self.serverIP)
            self.output = '%sConnected-> %s\n' % (self.output, self.serverIP)

        except socket.error:
            self.sock.close()
            self.sock = None

        if self.sock is None:
            print  'Could not connect'
            self.output = '%sCould not connect.\n' % (self.output)

    def _disconn_button_changed(self):
        print 'Closing ....', self.serverIP
        self.sock.close()
        self.output = '%sClosing-> %s\n' % (self.output, self.serverIP)

    def _testconnect(self):
        if not isinstance(self.sock, socket.socket):
            self.output = '%sPlease connect HSM First\n' % (self.output)
            return False

        else:
            return True

    def _EncPIN_button_changed(self):

        if self.PIN == '':
            self.output = 'Pin Value is null\n'
        elif self._testconnect():
            func = 'Generate PIN BLOCK,'
            msg_header = '0001'
            command_code = 'BA'
            pin_data = self.PIN + 'F'
            pan_data = self.pan[3:15]
            data = msg_header + command_code + pin_data + pan_data
            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.sock.send(message)
            self.Resp = self.sock.recv(1024)
            self.ENC_PIN = self.Resp[10:]
            print 'ENC_PIN->', self.ENC_PIN
            self.output = '%sENC_PIN:%s\n' % (self.output, self.ENC_PIN)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]
            return self.ENC_PIN

    def _DecPIN_button_changed(self):
        if self._testconnect():
            if self.ENC_PIN == '':
                self.output = 'Generate ENC_PIN first,Execute BA button\n'
            else:
                func = "Decrypt PIN,"
                msg_header = '0001'
                command_code = 'NG'

                data = msg_header + command_code + self.pan[3:15] + self.ENC_PIN
                x = str(hex(len(data)))
                x.split('x')
                z = str(x[2:])
                message_len = binascii.a2b_hex(z.zfill(4))
                message = message_len + data
                if DEBUG_ON:
                    print func, 'msg_send:', message

                self.sock.send(message)
                self.Resp = self.sock.recv(1024)
                self.PIN = self.Resp[10:14]
                self.output = '%sClear PIN:%s\n' % (self.output, self.PIN)
                if DEBUG_ON:
                    print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _PINLMK2ZPK_button_changed(self):
        if self._testconnect():
            func = "Translate a PIN from LMK to ZPK Encryption,"
            msg_header = '0001'
            command_code = 'JG'
            pin_block_format = '01'
            pan_data = self.pan[3:15]
            data = msg_header + command_code + self.ZPK + pin_block_format + pan_data + self.ENC_PIN

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.sock.send(message)
            self.Resp = self.sock.recv(1024)
            self.PIN_Block_ZPK = self.Resp[10:]
            self.output = '%sPIN_Block_ZPK:%s\n' % (self.output, self.PIN_Block_ZPK)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]
            return self.PIN_Block_ZPK


    def _genPVV_button_changed(self):
        if self._testconnect():
            self.ENC_PIN = self._EncPIN_button_changed()
            func = " Generate a VISA PIN Verification Value,"
            msg_header = '0001'
            command_code = 'DG'
            pvki = '1'
            pan_data = self.pan[3:15]
            data = msg_header + command_code + self.PVK + self.ENC_PIN + pan_data + pvki

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.PVV = self.Resp[10:]
            print  'PVV ->', self.PVV
            self.output = '%sPVV:%s\n' % (self.output, self.PVV)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _genCVV_button_changed(self):
        if self._testconnect():
            func = "Generate a VISA CVV,"
            msg_header = '0001'
            command_code = 'CW'
            service1 = '201'
            service2 = '000'
            data = msg_header + command_code + self.CVK + self.pan + ';' + self.expire_date + service1

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data

            if DEBUG_ON:
                print func, 'msg_send:', message

            self.sock.send(message)
            self.Resp = self.sock.recv(1024)
            self.CVV = self.Resp[10:13]
            self.output = '%sService-Code:%s\t CVV:%s\n' % (self.output, service1, self.CVV)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]
            data = msg_header + command_code + self.CVK + self.pan + ';' + self.expire_date + service2
            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data

            if DEBUG_ON:
                print func, 'msg_send:', message

            self.sock.send(message)
            self.Resp = self.sock.recv(1024)
            self.CVV = self.Resp[10:13]
            self.output = '%sService-Code:%s\t CVV:%s\n' % (self.output, service2, self.CVV)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _VerifyVISACVV_button_changed(self):
        if self._testconnect():
            func = "Decrypt PIN,"
            msg_header = '0001'
            command_code = 'CY'

            data = msg_header + command_code + self.CVK + self.CVV + self.pan + ";" + self.expire_date + "000"
            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.sock.send(message)
            self.Resp = self.sock.recv(1024)
            self.output = '%sVerifyVISACVV reponse: %s \n' % (self.output, self.Resp[2:10])
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _VerifyPinVISATPK_button_changed(self):
        if self._testconnect():
            func = "VerifyPinVISATPK,"
            msg_header = '0001'
            command_code = 'DC'

            data = msg_header + command_code + self.TPK + self.PVK + self.PIN_Block_TPK + "01" + \
                   self.pan[3:15] + '1' + self.PVV

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.output = '%s Verify a Terminal PIN Using the VISA mehtod:%sn' % (self.output, self.Resp[3:20])
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _VerifyPinVISAZPK_button_changed(self):
        if self._testconnect():
            func = "VerifyPinVISAZPK,"
            msg_header = '0001'
            command_code = 'EC'
            if self.PIN_Block_ZPK == '':
                self.PIN_Block_ZPK = self._PINLMK2ZPK_button_changed()

            data = msg_header + command_code + self.ZPK + self.PVK + self.PIN_Block_ZPK + "01" + \
                   self.pan[3:15] + '1' + self.PVV

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.output = '%sVerify an Interchange PIN Using the VISA mehtod:%s\n' % (self.output, self.Resp[3:20])
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _ZPKZMK2LMK_button_changed(self):
        if self._testconnect():
            func = "VerifyPinVISAZPK,"
            msg_header = '0001'
            command_code = 'FA'

            data = msg_header + command_code + self.ZMK + self.ZPK_ZMK

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.output = '%sTranslate a ZPK from ZMK to LMK Encryptio:%s\n' % (self.output, self.Resp[8:43])
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]

    def _GenPINOffset_button_changed(self):
        if self._testconnect():
            func = "Derive a PIN Using the IBM Method,"
            msg_header = '0002'
            command_code = 'EE'
            offset = '0000FFFFFFFF'
            check_length = '04'
            Decimalisation_table = '0123456789012345'
            pin_validation_data = '00000000000N'
            data = msg_header + command_code + self.PVKX + offset + check_length + \
                   self.pan[3:15] + Decimalisation_table + pin_validation_data

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.ENC_PIN = self.Resp[10:15]
            self.output = '%sDerive a PIN Using the IBM Method,return-code:%s,PIN_BlockLMK value:%s\n' \
                          % (self.output, self.Resp[8:10], self.ENC_PIN)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]


    def _GenRandomPIN_button_changed(self):
        if self._testconnect():
            func = "GenRandomPIN,"
            msg_header = '0001'
            command_code = 'JA'

            data = msg_header + command_code + self.pan[3:15] + '04'

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.ENC_PIN = self.Resp[10:15]
            self.output = '%sGenerate Random PIN,return-code:%s,PIN value:%s\n' \
                          % (self.output, self.Resp[8:10], self.ENC_PIN)
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]


    def _VerifyARQC_button_changed(self):
        if self._testconnect():
            func = "Verify ARQC and Generate ARPC,"
            msg_header = '0001'
            command_code = 'KQ'
            chipdata1 = '795287000203010002160C516338323800000000010000000000000001'
            chipdata2 = '5880800080000901110525000C5163381800021603A00000'
            chipdata3 = '0000003BD2E032C8948E55A5303000'
            data = msg_header + command_code + "10" + self.MDK + binascii.a2b_hex(chipdata1 + chipdata2 + chipdata3)

            x = str(hex(len(data)))
            x.split('x')
            z = str(x[2:])
            message_len = binascii.a2b_hex(z.zfill(4))
            message = message_len + data
            self.sock.send(message)
            if DEBUG_ON:
                print func, 'msg_send:', message

            self.Resp = self.sock.recv(1024)
            self.output = '%sVerify ARQC and Genrate ARPC,return-code:%s, ARPC:%s\n' \
                          % (self.output, self.Resp[2:10], str.upper(binascii.b2a_hex(self.Resp[10:18])))
            if DEBUG_ON:
                print func, 'msg_recv:', self.Resp[0:len(self.Resp)]


if __name__ == '__main__':
    hsm = HSM()
    # hsm.configure_traits()
    hsm.configure_traits(view='view1')
    
