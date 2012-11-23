from  enthought.traits.api import * 
from  enthought.traits.ui.api import * 
from  enthought.traits.ui.menu import * 
import binhex,binascii,base64
import time


""" Using Base64 to decode / encode message 
    it will depening on your VISA/MCD ,to assemble CVV value 
    Author: Ray Yeh 2008/12/02"""

class Base64(HasTraits):
      option= Enum('D','E')
      card_type=Enum('V','M')
      input_text=Str
      display=Str
      intro= Str      
      code_button=Button()
      decode_result=''
      ct_value =Str
      
            
      view1=View(Group(Item('option',label='Choice your function,[E]Encode, [D]Decode:'),
                       Item('card_type',label='Select your CAVV [V]isa ,[M]asterCard:'),
                       Item('input_text',label='Type your message',style='custom'),
                       Item('display',style='custom'), 
                       Group(Item('code_button',label="Encode/Decode")),                      
                       label='Test Base64 tools v1.1',
                       show_border=True                       
                    ),
                kind='live',
                buttons=OKCancelButtons,
                width=800,height=600, 
                resizable=True,              
                title='Base64 Encoder tool v1.1'
                )      
      def dec2hex(self,n):
        """return the hexadecimal string representation of integer n"""
        return "%X" % n   

      def hex2dec(self,s):
        """return the integer value of a hexadecimal string s"""      
        return int(s, 16)

      def mcd(self):
          self.ct_value=str(self.hex2dec(self.decode_result[0:2]))
          self.display="----- MasterCard Base64 Decoding message ---\n\
          1.Control_type %s \n\
          2.HMAC= %s \n\
          3.ACS identify= %s\n\
          4.Auth-Method= %s \n\
          5.Bin-identify= %s\n\
          6.Transaction-seq=%s\n\
          7.MAC= %s\n\
          8.Expire-date(yymm)= %s\n\
          9.Cvv = %s\n\
          10.Service-Code= %s\n\
          11.Decode message=%s"\
          %(self.decode_result[0:2],self.decode_result[2:18],\
            self.decode_result[18:20],self.decode_result[20:21],\
            self.decode_result[21:22],self.decode_result[22:30],\
            self.decode_result[30:40],self.hex2dec(self.decode_result[22:30]),\
            self.decode_result[31:34],self.decode_result[20:21]+self.ct_value[1:],\
            self.decode_result) 
        
        
      def visa(self): 
          self.display= '----- VISA Base64 Decoding message ---\n\
          1.3D Secure Authentication Results Code= %s\n\
          2.Second Factor Authentication Code= %s\n\
          3.CAVV Key Indicator= %s\n\
          4.CVV output= %s\n\
          5.Unpredicactable number=%s\n\
          6.Authencation Tracking Number=%s\n\
          7.Expire-date(yymm)=%s\n\
          8.Cvv = %s\n\
          9.Service-Code=%s\n\
          10.Decode message=%s'\
          %(self.decode_result[0:2],self.decode_result[2:4],\
            self.decode_result[4:6],self.decode_result[6:8],\
            self.decode_result[10:14],self.decode_result[14:30],\
            self.decode_result[10:14],self.decode_result[7:10],\
            self.decode_result[1:4],self.decode_result)
       
   
      def _code_button_changed(self):
          if  self.option  in ['E']:              
              self.even=divmod(len(self.input_text),2)
              if self.even[1] <> 0:
                  self.display = "Len of Encode message is not EVEN"
              elif self.input_text.isalnum() == False:
                  self.display = "Encode message MUST alphanumeric"
              else:
                  self.display=binascii.b2a_base64(binascii.a2b_hex(self.input_text))              
          elif self.option in ['D']:
              self.even=divmod(len(self.input_text),2)
              if self.even[1] <> 0:
                  self.display = "Len of Decode message is not EVEN"
              else:                            
                  self.decode_result=binascii.b2a_hex(binascii.a2b_base64(self.input_text))              
                  if self.card_type in ['V']:
                      self.visa()
                  elif self.card_type in ['M']:
                      self.mcd()       

if __name__ == '__main__':
    #import psyco
    #psyco.full()
    start=time.time()
    a=Base64()
    a.configure_traits(view='view1')
    print  (time.time() - start)