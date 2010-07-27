validkeys = (1,2,3)
keyGenDict={'keys':[1,2,3],1:'blue',2:'fast',3:'test','key':2}

def show_key (key):
    if(key in validkeys):
        keyVal = (keyGenDict["keys"])[key-1]
        print "Key = " + keyGenDict[keyVal]
    else:
        print("Invalid key")

#Retrieving dictionary key list
print keyGenDict.keys()

#Retrieving dictionary value list
print keyGenDict.values()

#Retrieving dictionary value list
print keyGenDict.items()

#Retrieve value from key
val = keyGenDict["key"]
show_key(val)

keyGenDict["key"] = 1
val = keyGenDict["key"]
print val
print keyGenDict.items()
show_key(val)

numbers = ('1','2','3','4','5','6','7','8','9','0')
letters = ('a','b','c','d','e','f')
punct = ('.', '!', '?')
charSetDict = {numbers:'x', letters:'y', punct:'z'}
print charSetDict.items()
print charSetDict.keys()
print charSetDict.values()
print charSetDict.has_key(numbers)
print charSetDict[numbers] #get numbers value


print '#' * 80
year = {1:'January', 2:'February', 3:'March',4:'April',\
        5:'May', 6:'June', 7:'July', 8:'August',\
        9:'September', 10:'October', 11:'November',\
        12:'December'}

print year

months=year.keys()
half_year= months[0:len(months)/2]
print half_year

mon={}
for x in half_year:
    mon[x]=year[x]

print mon

print '='*60
myDictionary = {'color':'blue', 'speed':'fast',
 'number':1, 5:'number'}

print myDictionary

#Swap keys for values
swapDictionary = {}
for key, val in myDictionary.iteritems():
    swapDictionary[val] = key

print swapDictionary

print '='*60
word1='A'
word2='B'
word3=['A','B','C']
print 'Word'+word1+word2
print 'Word1'.join(word3)

print '='*60
Sstring = "I am good ab cd you are best"
print Sstring.find("good")
print Sstring.rfind("best")
print Sstring.find("I")
print Sstring.index("good")
Rstring=Sstring.replace("good","bad") # Replace string from good ,by bad
print Rstring

########################
print '='*60
import os

for f in os.listdir('D:\\'): #找尋D 底下的資料
    if f.endswith('.exe'):  #找出 exe 的附檔名
        print "Exe file: " + f
    elif f.endswith('.txt'):
        print "Text file: " + f

###############################################
#demo  如何移除不必要字元 strip()
print '='*60
import string
badSentence = "\t\tThis sentence has problems.   "

badParagraph = "\t\tThis paragraph \nhas even \
    more \nproblems.!?   "

#Strip trailing spaces
print "Length = " + str(len(badSentence))
print "Without trailing spaces = " + \
    str(len(badSentence.rstrip(' ')))

#Strip tabs
print "\nBad:\n" + badSentence
print "\nFixed:\n" + badSentence.lstrip('\t')

#Strip leading and trailing characters
print "\nBad:\n" + badParagraph
print "\nFixed:\n" + badParagraph.strip((' ?!\t'))


###############################################
print '='*60
print "Demo: 左靠還是右靠"
chapters = {1:5, 2:46, 3:52, 4:87, 5:90}
hexStr = "3f8"

#Right justify  rjust(width,fill)
print "Hex String: " + hexStr.upper().rjust(8,'0')
print
for x in chapters:
    print "Chapter " + str(x) + \
        str(chapters[x]).rjust(15,'.')


#Left justify ljust(width,fill)
print "\nHex String: " + hexStr.upper().ljust(8,'0')

#String format
print
for x in chapters:
    print "Chapter %d %15s" % (x,str(chapters[x]))
###############################################
## Demo:exec(str [,globals [,locals]]) 
print '='*60
cards = ['Ace', 'King', 'Queen', 'Jack']
codeStr = "for card in cards: \
    print \"Card = \" + card"

#Execute string
exec(codeStr)
####################################################
import string

values = [5, 3, 'blue', 'red']
s = string.Template("Variable v = $v") #Template(string) method

for x in values:
    print s.substitute(v=x) #substitute(m, [, kwargs])
    
