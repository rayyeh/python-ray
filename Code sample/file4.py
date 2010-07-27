-*-  coding :UTF-8  -*-
###############################################
## Demo: file open 
print '='*60
#rU => U is The universal newline mode converts
#      all the different variations (\r, \n, \r\n)
#      to the standard \n character

filePath = "c:/input.txt"

#Read entire file into a buffer
buffer = "Read buffer:\n"
buffer += open(filePath, 'rU').read()
print buffer

#Read lines into a buffer
buffer = "Readline buffer:\n"
inList = open(filePath, 'rU').readlines()
print inList
for line in inList:
    buffer += line
print buffer

#Read bytes into a buffer
buffer = "Read buffer:\n"
file = open(filePath, 'rU')
while(1):
    bytes = file.read(10)
    if bytes:
        buffer += bytes
    else:
        break

print buffer

##################################################
print '='* 80
filePath = "c:/input.txt"
wordList = []
wordCount = 0

#Read lines into a list
file = open(filePath, 'rU')
for line in file:
    for word in line.split():
        wordList.append(word)
        wordCount += 1
print wordList
print "Total words = %d" % wordCount
####################################################
print '='* 80
wordList = ["Red", "Blue", "Green"]
filePath = "C:/output.txt"

#Write a list to a file
file = open(filePath, 'w+')
file.writelines(wordList)

#Write a string to a file
file.write("\n\nFormatted text:\n")

#Print directly to a file
for word in wordList:
    print >>file,"\t%s Color Adjust" %word

file.close()
############################################################
print '=' *80
print "列出所有目錄下的檔名"
## for each directory in the tree create a three-tuple
## containing (1) the dirpath, (2) a list of dirnames, and (3) a list of filenames
import os
path = "d:/cmmi"

def printFiles(dirList, spaceCount):
    for file in dirList:
        print "/".rjust(spaceCount+1) + file

def printDirectory(dirEntry):
    print dirEntry[0] + "/"
    printFiles(dirEntry[2], len(dirEntry[0]))
       

tree = os.walk(path)
for directory in tree:
    printDirectory(directory)
############################################################
print '#' * 80
import os

FileName= open('c:/1.txt','w+')
FileName.close()
oldFileName = "c:/1.txt"
newFileName = "c:/1_old.txt"

#Old Listing
for file in os.listdir("c:/"):
    if file.startswith("output"):
        print file

#Remove file if the new name already exists
if os.access(newFileName, os.X_OK):
    print "Removing " + newFileName
    os.remove(newFileName)

#Rename the file
os.rename(oldFileName, newFileName)

#New Listing
for file in os.listdir("c:/"):
    if file.startswith("output"):
        print file
########################################
### Warming : It will remove directory
########################################        
import os


emptyDirs = []
path = "/trash/deleted_files"

def deleteFiles(dirList, dirPath):
    for file in dirList:
        print "Deleting " + file
        os.remove(dirPath + "/" + file)

def removeDirectory(dirEntry):
    print "Deleting files in " + dirEntry[0]
    deleteFiles(dirEntry[2], dirEntry[0])
    emptyDirs.insert(0, dirEntry[0])

print "It will delete your directory:"+ path     
answer=raw_input(" Say Y or N" )

if answer == 'N':
    print 'Stop run'
else: 
    print 'Begin delete directory:  ' + path    
    #Enumerate the entries in the tree
    tree = os.walk(path)
    for directory in tree:
        removeDirectory(directory)

    #Remove the empty directories
    for dir in emptyDirs:
        print "Removing " + dir
        os.rmdir(dir)

###################################################
import os
path = "d:/python25"
pattern = "*.py;*.doc"

#Print files that match to file extensions
def printFiles(dirList, spaceCount, typeList):
    for file in dirList:
        for ext in typeList:
            if file.endswith(ext):
                print "/".rjust(spaceCount+1) + file
                break

#Print each sub-directory
def printDirectory(dirEntry, typeList):
    print dirEntry[0] + "/"
    printFiles(dirEntry[2], len(dirEntry[0]),typeList)

#Convert pattern string to list of file extensions
extList = []
for ext in pattern.split(";"):
    extList.append(ext.lstrip("*"))

#Walk the tree to print files
for directory in os.walk(path):
    printDirectory(directory, extList)






