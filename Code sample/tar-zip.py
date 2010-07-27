#################################################
# Demo:Creating a TAR File
#################################################
print 'Demo: Creating a TAR File'
import os
import tarfile

#Create Tar file
tFile = tarfile.open("files.tar", 'w')

#Add directory contents to tar file
files = os.listdir(".")
for f in files:
    tFile.add(f)

#List files in tar
for f in tFile.getnames():
    print "Added %s" % f

tFile.close()

############################################
###Demo :Extracting a File from a TAR File
############################################
print 'Demo: Extracting a File from a TAR File'
import os
import tarfile

# Extract path
extractPath = ".\ext"

#Open Tar file
tFile = tarfile.open("files.tar", 'r')

#Extract py files in tar
for f in tFile.getnames():
    if f.endswith("py"):
        print "Extracting %s" % f
        tFile.extract(f, extractPath)
    else:
        print "%s is not a Python file." % f

tFile.close()
