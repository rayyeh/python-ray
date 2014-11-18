#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
   SVNMD5.EXE.
   Used to compare working copy and Repository  ,genereate compare report.
   It's 100 %  Python :)
   I use Python 2.6.4 , py2exe,pysvn 1.7.2 to create SVNMD5.EXE
   Diff report format : Unified diff format
"""

__author__ = ' Ray Yeh <yeh_ray@hotmail.com>'
__version__ = '1.0'
__licence__ = 'GPL V3'

import sys
import os
import re
from datetime import datetime
import codecs
import hashlib

import pysvn


def Usage():
    print """Usage: """ + sys.argv[0] + """ PATH  >>  Report_file
Usage sample1 : SVNMD5.exe d:\project >>  d:\svnreport.txt   --> Output report at d:\svnreport.txt
Usage sample 2: SVNMD5.exe d:\project   --> Output at screen
Batch compare working copy with repository  and generate report to PATH

by  Ray Yeh    version 1.0
   """
    sys.exit(1)

# ------------------------------- Process the options -------------------------
if len(sys.argv) == 2:
    workingdir = sys.argv[1]
else:
    Usage()

try:
    os.chdir(workingdir)
except OSError:
    print "Cannot change dir to " + workingdir
    Usage()
#------------------------------- Find out what has changed -------------------
client = pysvn.Client()
changes = client.status(workingdir)

#print 'files to be added:'
addedlist = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.added]
#print 'files to be removed:'
deletedlist = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.deleted]
#print 'files that have changed:'
modifiedlist = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.modified]
#print 'files with merge conflicts:'
conflictedlist = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.conflicted]
#print 'unversioned files:'
unversionedlist = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.unversioned]
#print 'missing files:'
missinglist = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.missing]

dt = datetime.now()

print "SVN compare run at:" + dt.strftime("%A, %d. %B %Y %I:%M%p")
print "Compare Woking directory:" + workingdir + "\n"

str_1 = u"================== 產生 Compare 資料開始 ================="
str_2 = u"================== 產生 Compare 資料結束 ================="
print  str_1.encode('big5_tw')
#  Added  files
for item in addedlist:
    buff = ""
    file = open(item, 'rb')
    buff = file.read()
    file.close()
    m = hashlib.sha1()
    m.update(buff)
    print item + " =>SHA1  Chksum:" + m.hexdigest()

#Modified files
for item in modifiedlist:
    buff = ""
    file = open(item, 'rb')
    buff = file.read()
    file.close()
    m = hashlib.sha1()
    m.update(buff)
    print item + " =>SHA1 Chksum:" + m.hexdigest()
print  str_2.encode('big5_tw')

#Unversionedl files
for item in unversionedlist:
    buff = ""
    file = open(item, 'rb')
    buff = file.read()
    file.close()
    m = hashlib.md5()
    m.update(buff)
    print item + " =>MD5 Chksum:" + m.hexdigest()

deletedcount = 0
modifiedcount = 0
missingcount = 0
addedcount = 0
unversionedcount = 0

i = 0
for i in addedlist:
    addedcount += 1
i = 0
for i in modifiedlist:
    modifiedcount += 1
i = 0
for i in missinglist:
    missingcount += 1
i = 0
for i in unversionedlist:
    unversionedcount += 1

str_3 = u'比對目錄路徑:'
str_4 = u'比對檔案清單:'
str_5 = u'新增   '
str_6 = u'差異   '
str_7 = u'刪除   '
str_8 = u'未納版'
print str_3.encode('big5_tw')
print str_4.encode('big5_tw')
print str_5.encode('big5_tw') + '%d folders/files:\n%s' % (addedcount, addedlist)
print str_6.encode('big5_tw') + '%d folders/files:\n%s' % (modifiedcount, modifiedlist)
print str_7.encode('big5_tw') + '%d folders/files:\n%s' % (missingcount, missinglist)
print str_8.encode('big5_tw') + '%d folders/files:\n%s' % (unversionedcount, unversionedlist)
print "==========================================================" 
