""" Using Base64 to decode / encode message 
    it will depening on your VISA/MCD ,to assemble CVV value 
    Author: Ray Yeh 2008/12/02"""
from builtins import str
from builtins import input


def base64():
    import binhex, binascii, base64

    def dec2hex(n):
        """return the hexadecimal string representation of integer n"""
        return "%X" % n

    def hex2dec(s):
        """return the integer value of a hexadecimal string s"""
        return int(s, 16)

    def decode(codeopt):
        print 'Your Encode txt: ' + codeopt
        data_result = binascii.b2a_hex(binascii.a2b_base64(codeopt))
        print 'Your Decode txt:' + data_result
        return data_result

    def encode(codeopt):
        print 'You decode txt:' + codeopt
        print 'Your Ecnode txt:' \
              + binascii.b2a_base64(binascii.a2b_hex(codeopt))

    def cardtype(data_result):
        """ disassemble VISA /MasterCard CAVV value"""
        type = input('Select your CAVV [V]isa ,[M]asterCard:')
        if type in ['M', 'm']:
            mcd(data_result)
        if type in ['V', 'v']:
            visa(data_result)

    def mcd(data_result):
        print '--- MasterCard CAVV value -----------'
        print '1.Control_type]=' + data_result[0:2] + \
              ' 2.HMAC=' + data_result[2:18]
        print '3.ACS identify=' + data_result[18:20] + \
              ' 4.Auth-Method=' + data_result[20:21]
        print '5.Bin-identify=' + data_result[21:22] + \
              ' 6.Transaction-seq=' + data_result[22:30]
        print '7.MAC=' + data_result[30:40]
        print '--- Mastercard Cvv data  Begin-----'
        print 'Expire-date(yymm)=', hex2dec(data_result[26:30])
        print 'Cvv =' + data_result[31:34]
        ct_value = str(hex2dec(data_result[0:2]))
        print 'Service-Code=' + data_result[20:21] + ct_value[1:]
        print '--- Mastercard Cvv data  End-----'

    def visa(data_result):
        print '--- VISA CAVV value -----------'
        print '1.3D Secure Authentication Results Code=' + data_result[0:2]
        print '2.Second Factor Authentication Code=' + data_result[2:4]
        print '3.CAVV Key Indicator=' + data_result[4:6]
        print '4.CVV output=' + data_result[6:10]
        print '5.Unpredicactable number=' + data_result[10:14]
        print '6.Authencation Tracking Number=' + data_result[14:30]
        print '--- Visa Cvv data  Begin-----'
        print 'Expire-date(yymm)=' + data_result[10:14]
        print 'Cvv =' + data_result[7:10]
        print 'Service-Code=' + data_result[1:4]
        print '--- Visa Cvv data ------'

    while 1:
        print '*' * 40
        print 'Demo VISA/MasterCard Base64 functtion,'
        print 'Author: Ray Yeh        Date:2008/12/02'
        print 'Usage :'
        print '  1, Choice [E]Encode, [D]Decode'
        print '  2, Key in Encode or Decode message'
        print '  3, If you select [D]ecode ,you need to choice [V]isa'
        print '     [M]cd card, it will tell you Cvv component \n'
        print 'If you want to exit, Press CTRL-Z'
        print '   Encode sample:jDThYQgCOUfeCBgAABOCB0MAAAA='
        print '   Decode sample:8c34e16108023947de0818000013820743000000'
        print '*' * 40

        option = input('Choice your function,[E]Encode, [D]Decode:')

        if option in ['D', 'd']:
            codeopt = input('Type your Decode message(28 bytes) :')
            if len(codeopt) == 28:
                data_result = decode(codeopt)
                cardtype(data_result)

        elif option in ['E', 'e']:
            codeopt = input('Type your Encode message(40 bytes) :')
            if len(codeopt) == 40:
                encode(codeopt)
        else:
            print 'You  do not select [E]ncode,[D]ecode'

        exit = input('Will continute,[N]o exit, [Y] contine:')
        if exit in ['N', 'n']:
            break


if __name__ == "__main__":
    base64()

