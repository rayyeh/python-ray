# -*- coding: UTF-8 -*-
# Credit card Check in system , Creator by Ray Yeh, Version :1.0 
# It use SQLITE to perform  check/logging


import SocketServer
import time
import string
import binascii
import datetime
import sqlite3
import os

myHost = ''
myPort = 5052

_version_ = 1.0
_author_ = 'Ray Yeh'
PROJECT_PATH = os.path.abspath(os.path.dirname('.'))

DB_PATH = os.path.join(PROJECT_PATH, 'python1.sqlite')


def now():
    return time.ctime(time.time())


class MyClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'Welcome Clinet:', self.client_address, now()
        while True:

            conn = sqlite3.connect(DB_PATH)

            msg_in = self.request.recv(1024)
            time.sleep(1)
            if not msg_in: break

            #process bitmap data 
            def bitmap(msg):
                bitmap = (binascii.b2a_hex(msg[9:17]))
                bitmap_b2h = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', \
                              '0101': '5', '0110': '6', '0111': '7', '1000': '8', \
                              '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', \
                              '1110': 'e', '1111': 'f'}

                bitmap_h2b = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '1000', \
                              '5': '1001', '6': '1010', '7': '1011', '8': '1100', \
                              '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', \
                              'e': '1110', 'f': '1111'}

                #datatable ={1:[Fixed or Dynamic,Binary or Nible or Char, Max length]}
                ISO8583 = {1: ['f', 'b', 64], 2: ['d', 'n', 19], 3: ['f', 'n', '6'], 4: ['f', 'n', '12'], \
                           5: ['f', 'n', 12], 6: ['f', 'n', 12], 7: ['f', 'n', 10], 8: ['f', 'n', 8], \
                           9: ['f', 'n', 8], 10: ['f', 'n', 9], 11: ['f', 'n', 6], 12: ['f', 'n', 6], \
                           13: ['f', 'n', 4], 14: ['f', 'n', 4], 15: ['f', 'n', 4], 16: ['f', 'n', 4], \
                           17: ['f', 'n', 4], 18: ['f', 'n', 4], 19: ['f', 'n', 4], 20: ['f', 'n', 4], \
                           21: ['f', 'n', 4], 22: ['f', 'n', 4], 23: ['f', 'n', 4], 24: ['f', 'n', 4], \
                           25: ['f', 'n', 2], 26: ['f', 'n', 2], 27: ['f', 'n', 2], 28: ['f', 'n', 8], \
                           29: ['f', 'n', 8], 30: ['f', 'n', 8], 31: ['f', 'n', 4], 32: ['d', 'n', 12], \
                           33: ['d', 'n', 12], 34: ['d', 'n', 28], 35: ['d', 'z', 37], 36: ['d', 'n', 104], \
                           37: ['f', 'a', 12], 38: ['f', 'a', 6], 39: ['f', 'a', 2], 40: ['f', 'a', 3], \
                           41: ['f', 'a', 8], 42: ['f', 'a', 15], 43: ['f', 'a', 40], 44: ['d', 'a', 44], \
                           45: ['d', 'a', 76], 46: ['f', 'a', 999], 47: ['f', 'a', 999], 48: ['f', 'a', 999], \
                           49: ['f', 'a', 3], 50: ['f', 'a', 3], 51: ['f', 'a', 3], 52: ['f', 'b', 16], \
                           53: ['f', 'n', 18], 54: ['f', 'a', 120], 55: ['f', 'a', 999], 56: ['f', 'a', 999], \
                           57: ['f', 'a', 999], 58: ['f', 'a', 999], 59: ['f', 'a', 999], 60: ['f', 'a', 7], \
                           61: ['f', 'a', 999], 62: ['f', 'a', 999], 63: ['f', 'a', 999], 64: ['f', 'b', 16]}

                #parser Bitmap 
                bitmaplist = ''
                for item in bitmap:
                    bitmaplist = bitmaplist + bitmap_h2b[item]
                    #print 'BitMap result :', bitmaplist

            def trantime():
                trantime = time.strftime("%H%M%S", time.localtime())
                trandate = time.strftime("%m%d")
                date_ymd = time.strftime("%y%m%d")
                return (date_ymd, binascii.a2b_hex(trantime), binascii.a2b_hex(trandate))


            def tpdu(msg):  # process TPDU header 
                tpdu_type = msg[2:3]
                tpdu_from = msg[3:5]
                tpdu_to = msg[5:7]
                tpdu = tpdu_type + tpdu_to + tpdu_from
                return tpdu


            def msgtype(msg):  #process message type and convert reponse message type
                msgtype = (binascii.b2a_hex(msg[7:9]))
                if msgtype[2] == '0':
                    msgtype = msgtype[0:2] + '10'
                else:
                    msgtype = msgtype[0:2] + '30'
                return binascii.a2b_hex(msgtype)


            #Stripe card
            def mag(msg):
                import binascii
                #print now()                
                F3_processcode = msg[17:20]
                F4_amt = msg[20:26]
                F11_traceno = msg[26:29]
                F11_traceno_hex = binascii.b2a_hex(msg[26:29])
                F22_PosEntryMode = msg[29:31]
                F24_NII = msg[31:33]
                F25_PosConCode = msg[33:34]
                F35_TrackII = msg[35:51]
                F41_TID = msg[51:59]
                F42_MID = msg[59:76]
                F48_data = msg[74:91]
                F48_PID = msg[76:91]

                def magdisplay():
                    print '*** Mag message Start ***'
                    print ' F3:', binascii.b2a_hex(F3_processcode)
                    print ' F4:', binascii.b2a_hex(F4_amt)
                    print ' F11_traceno:', binascii.b2a_hex(F11_traceno)
                    print ' F22_PosEntryMode:', binascii.b2a_hex(F22_PosEntryMode)
                    print ' F24_NII:', binascii.b2a_hex(F24_NII)
                    print ' F25_PosConCode:', binascii.b2a_hex(F25_PosConCode)
                    print ' F35_TrackII:', binascii.b2a_hex(F35_TrackII)
                    print ' F41_TID:', F41_TID
                    print ' F42_MID:', F42_MID, '\n\t'
                    print ' F48_PID:', F48_PID
                    print '*** Mag message End  ***'

                magdisplay()

                #format reponse message header and Get F12/F13/F37 
                tpdu_out = tpdu(msg)
                msgtype_out = msgtype(msg)
                F37_ymd, F12_trantime, F13_trandate = trantime()

                card_txt = binascii.b2a_hex(F35_TrackII[0:11])
                card = card_txt[0:16]
                card_expire = card_txt[17:21]

                today = datetime.date.today()
                now = datetime.datetime.now()

                c = conn.cursor()
                error = 0

                #Read sqlite DB ,check tid  and pid is match
                if error == 0:
                    c.execute("select * from tid where tid=? and pid =?", (F41_TID, F48_PID))
                    result = c.fetchone()
                    if result == None:
                        error = 1
                        print 'Fail on checking tid', F41_TID, F48_PID
                        F39_resp = '05'
                    else:
                        error = 0
                else:
                    pass

                #Read sqlite DB ,check prog id is active    
                if error == 0:
                    c.execute("select * from prog where pid=? and startdate <= ? and enddate >=?",
                              (F48_PID, today, today))
                    result = c.fetchone()[5]
                    if result == None:
                        error = 1
                        print 'Fail on checking prog', F48_PID, today
                        F39_resp = '66'
                    else:
                        rule = result
                        print "Rule value", rule
                        error = 0
                else:
                    pass

                    #Read sqlite DB,Check PAN table
                #If rule is  by card (rule =0) 
                #If rule is  by sid  (rule =1)                                  
                if error == 0:
                    c.execute("select * from pan where pan =? and expiredate =? and pid=?",
                              (card, card_expire, F48_PID))
                    result = c.fetchone()
                    print result
                    if result == None:
                        print 'Fail on checking pan:', card
                        error = 1
                        F39_resp = '64'
                    else:
                        sid = str(result[4])
                        print 'customer-id:', sid
                        error = 0
                    print rule, result[5], error
                    if result != None:
                        if rule == '0' and result[5] == 1 and error == 0:
                            print 'ByCard already checkin:', card
                            error = 1
                            F39_resp = '66'
                        elif rule == '0' and result[5] == 0 and error == 0:
                            error = 0
                        elif rule == '1' and error == 0:
                            c.execute("select * from pan where (sid =? or sid =?) and pid = ? order by checkin DESC ",
                                      (sid, str.upper(sid), F48_PID))
                            result = c.fetchone()
                            print result
                            if result[5] == 1:
                                print 'ByID already chekin:', sid
                                error = 1
                                F39_resp = '64'
                            else:
                                error = 0
                else:
                    pass

                    #final, format reponse message
                if error == 0:
                    print 'Check successfully '
                    bitmap_ok = binascii.a2b_hex('203801800e810000')
                    now = datetime.datetime.now()
                    F39_resp = '00'

                    #Generate auth number
                    today = datetime.date.today()
                    c.execute("select count (*) from tranlog where trandate='%s' and \
                     authno !=''" % today)
                    cnt = c.fetchone()[0]
                    cnt = cnt + 1
                    cntx = '000000'
                    F38_authno = cntx
                    F38_authno = cntx[:6 - len(str(cnt))] + str(cnt)
                    print F38_authno

                    #Generate RRN 
                    c.execute("select transeq from tid where tid='%s' " % F41_TID)
                    rrn = c.fetchone()[0]
                    rrn = rrn + 1
                    rrx = '000000'
                    F37_rrn = F37_ymd + rrx[:6 - len(str(rrn))] + str(rrn)
                    c.execute("update tid set transeq =? where tid=? ", (rrn, F41_TID))
                    conn.commit()

                    #Update pan ,already checkin 
                    c.execute("update pan set checkin=1,checkindate=?  where pan=?", \
                              (now, card))
                    conn.commit

                    #Write tranlog to record 
                    c.execute(
                        "insert into tranlog(trandate,trantime,tid,pad,resp,authno,traceno,reveflag) values (?,?,?,?,?,?,?,?,?)",
                        (today, datetime.datetime.now(), F41_TID, card, F48_PID, F39_resp, F38_authno, F11_traceno_hex,
                         0 ))
                    conn.commit()
                    c.close()

                    msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                              + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                              + F37_rrn + F38_authno + F39_resp + F41_TID + F48_data
                #final, format and reponse error  message                       
                if error:
                    print 'Check Fail '
                    bitmap_ok = binascii.a2b_hex('203801800a810000')
                    if F39_resp == '05':
                        F37_rrn = ''
                    else:
                        #Generate RRN 
                        c.execute("select transeq from tid where tid='%s' " % F41_TID)
                        rrn = c.fetchone()[0]
                        rrn = rrn + 1
                        rrx = '000000'
                        F37_rrn = F37_ymd + rrx[:6 - len(str(rrn))] + str(rrn)
                        c.execute("update tid set transeq =? where tid=? ", (rrn, F41_TID))
                        conn.commit()

                    F38_authno = ''
                    c.execute(
                        "insert into tranlog(trandate,trantime,tid,pad,resp,authno,traceno,reveflag) values (?,?,?,?,?,?,?,?,?)", \
                        (today, datetime.datetime.now(), F41_TID, card, F48_PID, F39_resp, F38_authno, F11_traceno_hex,
                         0 ))
                    conn.commit()
                    c.close()

                    msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                              + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                              + F37_rrn + F39_resp + F41_TID + F48_data

                return msg_txt


            #Manual key in 
            def manual(msg):
                #print now()
                import binascii

                F2_PAN = msg[18:26]
                F3_processcode = msg[26:29]
                F4_amt = msg[29:35]
                F11_traceno = msg[35:38]
                F11_traceno_hex = binascii.b2a_hex(msg[35:38])
                F14_expire = msg[38:40]
                F22_PosEntryMode = msg[40:42]
                F24_NII = msg[42:44]
                F25_PosConCode = msg[44:45]
                F41_TID = msg[45:53]
                F42_MID = msg[53:68]
                F48_data = msg[68:74]
                F48_PID = msg[70:74]


                def manualdisplay():
                    print '*** Manual message Start ***'
                    print ' F2_PAN:', binascii.b2a_hex(F2_PAN)
                    print ' F3:', binascii.b2a_hex(F3_processcode)
                    print ' F4:', binascii.b2a_hex(F4_amt)
                    print ' F11_traceno:', binascii.b2a_hex(F11_traceno)
                    print ' F14_expire', binascii.b2a_hex(F14_expire)
                    print ' F22_PosEntryMode:', binascii.b2a_hex(F22_PosEntryMode)
                    print ' F25_PosConCode:', binascii.b2a_hex(F25_PosConCode)
                    print ' F41_TID:', F41_TID
                    print ' F42_MID:', F42_MID
                    print ' F48_PID:', F48_PID
                    print '*** Manual message End  ***'

                manualdisplay()

                #format reponse message header and Get F12/F13/F37 
                tpdu_out = tpdu(msg)
                msgtype_out = msgtype(msg)
                F37_ymd, F12_trantime, F13_trandate = trantime()

                card = binascii.b2a_hex(F2_PAN)
                card_expire = binascii.b2a_hex(F14_expire)

                today = datetime.date.today()
                now = datetime.datetime.now()

                c = conn.cursor()
                error = 0

                #Read sqlite DB ,check tid  and pid is match
                if error == 0:
                    c.execute("select * from tid where tid=? and pid =?", (F41_TID, F48_PID))
                    result = c.fetchone()
                    if result == None:
                        error = 1
                        print 'Fail on checking tid', F41_TID, F48_PID
                        F39_resp = '05'
                    else:
                        error = 0
                else:
                    pass

                #Read sqlite DB ,check prog id is active    
                if error == 0:
                    c.execute("select * from prog where pid=? and startdate <= ? and enddate >=?",
                              (F48_PID, today, today))
                    result = c.fetchone()[5]
                    if result == None:
                        error = 1
                        print 'Fail on checking prog', F48_PID, today
                        F39_resp = '66'
                    else:
                        rule = result
                        print "Rule value", rule
                        error = 0
                else:
                    pass

                    #Read sqlite DB,Check PAN table
                #If rule is  by card (rule =0) 
                #If rule is by sid(rule =1)                
                if error == 0:
                    c.execute("select * from pan where pan =? and expiredate =? and pid=?  ",
                              (card, card_expire, F48_PID))
                    result = c.fetchone()
                    if result == None:
                        print 'Fail on checking pan:', card
                        error = 1
                        F39_resp = '64'
                    else:
                        sid = str(result[4])
                        print sid
                        error = 0

                    if result <> None:
                        if rule == '0' and result[5] == 1 and error == 0:
                            print 'Already checkin:', card
                            error = 1
                            F39_resp = '66'
                        elif rule == '0' and result[5] == 0 and error == 0:
                            error = 0
                        elif rule == '1' and error == 0:
                            c.execute("select * from pan where (sid =? or sid=?)  and pid = ? order by checkin DESC ",
                                      (sid, str.upper(sid), F48_PID))
                            result = c.fetchone()
                            print result
                            if result[5] == 1:
                                print 'ID already chekin:', sid
                                error = 1
                                F39_resp = '64'
                            else:
                                error = 0
                else:
                    pass

                if error == 0:
                    print 'Check successfully'
                    bitmap_ok = binascii.a2b_hex('203801800e810000')
                    now = datetime.datetime.now()
                    F39_resp = '00'

                    #Generate auth number
                    today = datetime.date.today()
                    c.execute("select count (*) from tranlog where trandate='%s' and \
                     authno !=''" % today)
                    cnt = c.fetchone()[0]
                    cnt = cnt + 1
                    cntx = '000000'
                    F38_authno = cntx
                    F38_authno = cntx[:6 - len(str(cnt))] + str(cnt)


                    #Generate RRN 
                    c.execute("select transeq from tid where tid='%s' " % F41_TID)
                    rrn = c.fetchone()[0]
                    rrn = rrn + 1
                    rrx = '000000'
                    F37_rrn = F37_ymd + rrx[:6 - len(str(rrn))] + str(rrn)
                    c.execute("update tid set transeq =? where tid=? ", (rrn, F41_TID))
                    conn.commit()
                    print F37_rrn

                    #Update pan ,already checkin 
                    c.execute("update pan set checkin=1,checkindate=? where pan=?", \
                              (now, card))
                    conn.commit

                    #Write tranlog to record 
                    c.execute(
                        "insert into tranlog(trandate,trantime,tid,pad,resp,authno,traceno,reveflag) values (?,?,?,?,?,?,?,?,?)", \
                        (today, datetime.datetime.now(), F41_TID, card, F48_PID, F39_resp, F38_authno, F11_traceno_hex,
                         0 ))
                    conn.commit()
                    c.close()

                    msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                              + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                              + F37_rrn + F38_authno + F39_resp + F41_TID + F48_data

                if error:
                    print 'Check Fail '
                    bitmap_ok = binascii.a2b_hex('203801800a810000')
                    if F39_resp == '05':
                        F37_rrn = ''
                    else:
                        #Generate RRN 
                        c.execute("select transeq from tid where tid='%s' " % F41_TID)
                        rrn = c.fetchone()[0]
                        rrn = rrn + 1
                        rrx = '000000'
                        F37_rrn = F37_ymd + rrx[:6 - len(str(rrn))] + str(rrn)
                        c.execute("update tid set transeq =? where tid=? ", (rrn, F41_TID))
                        conn.commit()

                    F38_authno = ''
                    c.execute(
                        "insert into tranlog(trandate,trantime,tid,pad,resp,authno,traceno,reveflag) values (?,?,?,?,?,?,?,?,?)", \
                        (today, datetime.datetime.now(), F41_TID, card, F48_PID, F39_resp, F38_authno, F11_traceno_hex,
                         0 ))
                    conn.commit()
                    c.close()

                    msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                              + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                              + F37_rrn + F39_resp + F41_TID + F48_data

                return msg_txt

            #Reversal txn
            def reversal(msg):
                #print now()                
                F2_PAN = msg[18:26]
                F3_processcode = msg[26:29]
                F4_amt = msg[29:35]
                F11_traceno = msg[35:38]
                F11_traceno_hex = binascii.b2a_hex(msg[35:38])
                F14_expire = msg[38:40]
                F22_PosEntryMode = msg[40:42]
                F24_NII = msg[42:44]
                F25_PosConCode = msg[44:45]
                F41_TID = msg[45:53]
                F42_MID = msg[53:68]
                F48_data = msg[68:74]
                F48_PID = msg[70:74]

                def reversaldisplay():
                    print '*** Manual message Start ***'
                    print ' F2_PAN:', binascii.b2a_hex(F2_PAN)
                    print ' F3:', binascii.b2a_hex(F3_processcode)
                    print ' F4:', binascii.b2a_hex(F4_amt)
                    print ' F11_traceno:', binascii.b2a_hex(F11_traceno)
                    print ' F14_expire', binascii.b2a_hex(F14_expire)
                    print ' F22_PosEntryMode:', binascii.b2a_hex(F22_PosEntryMode)
                    print ' F25_PosConCode:', binascii.b2a_hex(F25_PosConCode)
                    print ' F41_TID:', F41_TID
                    print ' F42_MID:', F42_MID
                    print ' F48_PID:', F48_PID
                    print '*** Manual message End  ***'

                reversaldisplay()

                #format reponse message header and Get F12/F13/F37 
                tpdu_out = tpdu(msg)
                msgtype_out = msgtype(msg)
                F37_ymd, F12_trantime, F13_trandate = trantime()

                card = binascii.b2a_hex(F2_PAN)
                card_expire = binascii.b2a_hex(F14_expire)

                today = datetime.date.today()
                now = datetime.datetime.now()

                c = conn.cursor()
                error = 0

                #Find original tranlog 
                if error == 0:
                    c.execute("select * from tranlog where pan=? and tid=? and traceno=? and pid =? ",
                              (card, F41_TID, F11_traceno_hex, F48_PID ))
                    result = c.fetchone()
                    if result == None:
                        print 'Reversal tranlog not found', F41_TID, ' card:', F11_traceno_hex
                        error = 1
                        F39_resp = 'E1'
                    else:
                        error = 0

                if error == 0:
                    print 'Reversal successfully'
                    bitmap_ok = binascii.a2b_hex('203801800a810000')
                    now = datetime.datetime.now()
                    F39_resp = '00'

                    #Generate RRN 
                    c.execute("select transeq from tid where tid='%s' " % F41_TID)
                    rrn = c.fetchone()[0]
                    rrn = rrn + 1
                    rrx = '000000'
                    F37_rrn = F37_ymd + rrx[:6 - len(str(rrn))] + str(rrn)
                    c.execute("update tid set transeq =? where tid=? ", (rrn, F41_TID))
                    conn.commit()
                    print F37_rrn

                    #Update pan ,already checkin 
                    c.execute("update pan set checkin=0,checkindate=? where pan=?", \
                              (now, card))
                    conn.commit

                    #Write tranlog to record 
                    c.execute(
                        "insert into tranlog(trandate,trantime,tid,pad,resp,authno,traceno,reveflag) values (?,?,?,?,?,?,?,?,?)",
                        (today, datetime.datetime.now(), F41_TID, card, F48_PID, F39_resp, '', F11_traceno_hex, 1))
                    conn.commit()
                    c.close()

                    msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                              + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                              + F37_rrn + F39_resp + F41_TID + F48_data

                if error:
                    print 'Reversal Fail,But send ok to EDC'
                    bitmap_ok = binascii.a2b_hex('203801800a810000')

                    #Generate RRN                     
                    F37_rrn = '0' * 12
                    #Write tranlog to record 
                    c.execute(
                        "insert into tranlog(trandate,trantime,tid,pad,resp,authno,traceno,reveflag) values (?,?,?,?,?,?,?,?,?)",
                        (today, datetime.datetime.now(), F41_TID, card, F48_PID, F39_resp, '', F11_traceno_hex, 1))
                    conn.commit()
                    c.close()

                    msg_txt = tpdu_out + msgtype_out + bitmap_ok + F3_processcode + F11_traceno \
                              + F12_trantime + F13_trandate + F24_NII + F25_PosConCode \
                              + F37_rrn + F39_resp + F41_TID + F48_data

                return msg_txt

            import os

            today = datetime.date.today()

            filepath = 'c:/tracelog-' + str(today) + '.txt'
            file = open(filepath, 'a+')

            #Check transaction is Stripe or Manual txn
            stime = datetime.datetime.now()
            msg_in_len = len(msg_in[2:])
            bitmap(msg_in)

            msgtypex = (binascii.b2a_hex(msg_in[7:9]))
            print msgtype

            file.writelines(binascii.b2a_hex(msg_in))
            timetxt = ';' + now() + '\n'
            file.write(timetxt)

            if msg_in_len == 0x004e:  #Stripe card
                print '#Stripe card'
                print 'msg in:', binascii.b2a_hex(msg_in)
                msg_out = mag(msg_in)

            if msg_in_len == 0x0048 and msgtypex == '0100':  #Manual txn
                print '#Manual txn'
                print 'msg in:', binascii.b2a_hex(msg_in)
                msg_out = manual(msg_in)

            if msg_in_len == 0x0048 and msgtypex == '0400':  #reversal
                print '#reversal'
                print 'msg in:', binascii.b2a_hex(msg_in)
                msg_out = reversal(msg_in)


                #Compute len of message
            x = hex(len(msg_out))  #compute len of message
            x.split('x')  #0xaa ,
            b = x[2:]  #get aa
            header = '0000'
            header = header[:4 - len(b)] + b  # convert  TCPIP len of header

            txt = binascii.a2b_hex(header) + msg_out
            print 'msg out:', binascii.b2a_hex(txt)
            etime = datetime.datetime.now()
            rtime = etime - stime
            print 'Process time:', rtime

            file.writelines(binascii.b2a_hex(txt))
            timetxt = ';' + now() + ';' + 'Process time:' + str(rtime) + '\n'
            file.write(timetxt)
            file.close()

            self.request.send(txt)

        self.request.close()


myaddr = (myHost, myPort)
server = SocketServer.ThreadingTCPServer(myaddr, MyClientHandler)
print '***  Credit card Checkin system ,starting at  %s  ***  ' % now()
print '***  Version:%s, Author:%s ***' % (_version_, _author_)
print '***  Server address: %s, Port:  %s  ***' % (myHost, myPort)
server.serve_forever()

