# walkex.py; finds the total number of bytes, number of files and number
# of directories in a given directory tree, dtree (current directory if
# not specified); adapted from code by Leston Buell

# usage:
# python walkex.py [dtree_root]
import os
path = "D:\\RACAL"

for root,dirs,files in os.walk(path):
    for filename in files:
        print os.path.join(root,filename)