#####################################################
# Demo:Adding Files to a ZIP File
#####################################################
print 'Demo :Adding Files to a ZIP File'
import os
import zipfile

#Create the zip file
tFile = zipfile.ZipFile("files.zip", 'w')

#Write directory contents to the zip file
files = os.listdir(".")
print files

for f in files:
    tFile.write(f)

#List archived files
for f in tFile.namelist():
    print "Added %s" % f
tFile.close()
#####################################################
# Demo:Retrieving Files from a ZIP File
#####################################################
import os
import zipfile


tFile = zipfile.ZipFile("files.zip", 'r')

#List info for archived file
print tFile.getinfo("input.txt")

#Read zipped file into a buffer
buffer = tFile.read("1.txt")
print buffer

#Write zipped file contents to new file
f = open("extract.txt", "w")
f.write(buffer)
f.close()
tFile.close()


