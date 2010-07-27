#!/usr/bin/env python
# Python version of the bash shell "svnreport"

"""
   SVNREPORT.EXE.
   Used to compare working copy and Repository  ,genereate compare report.
   It's 100 %  Python :)
   I use Python 2.6.4 , GnuWin32 diffutils, py2exe to create SVNREPORT.EXE
   Diff report format is Context Format
"""

__author__ =  ' Ray Yeh <yeh_ray@hotmail.com>'
__version__ = '1.0'
__licence__ = 'GPL V3'


import sys
import os
import re
from datetime import datetime

def Usage():
   print """Usage: """ + sys.argv[0] + """ PATH  >>  Report_file
Usage sample1 : svnreport.exe d:\project >>  d:\svnreport.txt   --> Output report at d:\svnreport.txt
Usage sample 2: svnreport.exe d:\project   --> Output at screen
Batch compare working copy with repository  and generate report to PATH

by  Ray Yeh    version 1.0
   """
   sys.exit(1)

#------------------------------- Process the options -------------------------
if len(sys.argv)==2 :
   workingdir=sys.argv[1]
else:
   Usage()

try:
   os.chdir(workingdir)
except OSError:
   print "Cannot change dir to " + workingdir
   Usage()

#------------------------------- Find out what has changed -------------------

svnstatus=os.popen("svn status").readlines()

added=""
deleted=""
modified=""
commit_message=""

for line in svnstatus:

   matchObject=re.match(r"^\?\s*(.*)\n",line)
   if matchObject:
       added = added + "\"" + matchObject.group(1) + "\" "
       #print matchObject.group(1)
       commit_message += "added file " + matchObject.group(1) + "\n"
       
   matchObject=re.match(r"^\!\s*(.*)\n",line)  
   if matchObject:
       deleted = deleted + "\"" + matchObject.group(1) + "\" "
       commit_message += "deleted file " + matchObject.group(1) + "\n"
      
   matchObject=re.match(r"^\M\s*(.*)\n",line)   
   if matchObject:
       modified = modified + "\"" + matchObject.group(1) + "\" "
       commit_message += "modified file " + matchObject.group(1) + "\n"
      
'''if added:
   #os.system("svn diff  "+added)  
if deleted:
   print "deleted-"+deleted
   #os.system("svn diff  "+deleted)  '''
if modified:
   os.system('svn diff --diff-cmd diff -x "-c" ' +modified ) 


if not added:
        commit_message += "no added files\n"
if not deleted:
        commit_message += "no deleted files\n"
if not modified:
        commit_message += "no modified files\n"

modifiedcount =0
addedcount = 0
deletedcount=0

addedlist=added.split()
modifiedlist=modified.split()
deletedlist=deleted.split()

i=0
for i in addedlist:
    addedcount +=1   
i=0
for i in modifiedlist:
    modifiedcount +=1
i=0
for i in deletedlist:
    deletedcount +=1   

dt=datetime.now()
print "======================================================="
print "SVN compare run at:"+ dt.strftime("%A, %d. %B %Y %I:%M%p")
print "Compare Woking directory:"+workingdir
print "Add        %d folders/files:\n%s" %(addedcount, added)
print "Modified  %d folders/files:\n%s" %(modifiedcount, modified)
print "Deleted   %d folders/files:\n%s" %(deletedcount, deleted)
print "======================================================="
