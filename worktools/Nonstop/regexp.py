import re

filename =raw_input('Enter you search file:')
searchPatten1=raw_input("Enter your search patten1:")
searchPatten2=raw_input("Enter your search patten2:")

print '------------- Process Starting---------------'
try :
    file=open(filename,'r')
except IOError:
    print "Can not fine the ", filename
    print "Stop run"
    exit()    

count=0
sentence=''
regexp1 =re.compile(searchPatten1,re.IGNORECASE+re.VERBOSE)
regexp2 =re.compile(searchPatten2,re.IGNORECASE+re.VERBOSE)

for line in file:
    if line[18:23] == '\UITC' :
       if sentence != '':        
            result1=regexp1.search(sentence)
            result2=regexp2.search(sentence)
            if result1 and result2 :
                count +=1
                print count, ':', sentence
       sentence = ''
       sentence= line
    else:
        sentence =sentence+ line
          
print '--------------Process Ending----------------------'
file.close()

