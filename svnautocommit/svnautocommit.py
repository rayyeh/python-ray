#!/usr/bin/env python
# Python version of the bash shell "autocommit"

import sys
import os
import re


def Usage():
    print """Usage: """ + sys.argv[0] + """ PATH

Automatically commits the changes of svn working copy located in PATH
The new files are automatically added and the files that have been
removed are removed.

By Gael Varoquaux
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

svnstatus = os.popen("svn status").readlines()

added = ""
deleted = ""
modified = ""
commit_message = "autocommit: \n"

for line in svnstatus:

    matchObject = re.match(r"^\?\s*(.*)\n", line)
    if matchObject:
        added = added + "\"" + matchObject.group(1) + "\" "
        commit_message += "added file " + matchObject.group(1) + "\n"
    matchObject = re.match(r"^\!\s*(.*)\n", line)
    if matchObject:
        deleted = deleted + "\"" + matchObject.group(1) + "\" "
        commit_message += "deleted file " + matchObject.group(1) + "\n"
        matchObject = re.match(r"^\M\s*(.*)\n", line)
    if matchObject:
        modified = modified + "\"" + matchObject.group(1) + "\" "
        commit_message += "modified file " + matchObject.group(1) + "\n"

if added:
    print "adding " + added
    os.system("svn add " + added)
if deleted:
    print "deleting " + deleted
    os.system("svn delete " + deleted)

if not added:
    commit_message += "no added files\n"
if not deleted:
    commit_message += "no deleted files\n"
if not modified:
    commit_message += "no modified files\n"

commit_command = 'svn commit -m \"' + commit_message + '\"'
os.system(commit_command)
