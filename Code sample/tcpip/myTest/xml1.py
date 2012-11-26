
from xml.etree import ElementTree as etree

message="<?xml version='1.0' encoding ='Big5'?> \
    <SEND> \
                    <TxnID>SENDMSG \
                        <SEND-RETN-DATE>201211051234</SEND-RETN-DATE>\
                        <SEND-RETN-CODE>0000</SEND-RETN-CODE>\
                        <SEND-RETN-CODE-DESC>你好</SEND-RETN-CODE-DESC>\
                    </TxnID>\
                    <SYSMSG>\
                        <MSG-ID>0008962750</MSG-ID> \
                        <MSG-DESC></MSG-DESC> \
                    </SYSMSG>\
                </SEND>"

msg=message.replace("Big5","utf-8")
print msg
tree=etree.fromstring(msg)

#root=tree.getroot()
for node in tree.iter():
    print 'Node : %s,  Text : %s' %(node.tag,node.text)
    
    
