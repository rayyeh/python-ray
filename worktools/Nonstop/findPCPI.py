import re

filename = raw_input('Enter you search file:')
searchPatten1 = raw_input("Enter your search patten1:")
searchPatten2 = raw_input("Enter your search patten2:")

print '------------- Process Starting---------------'
try:
    file = open(filename, 'r')
except IOError:
    print "Can not fine the ", filename
    print "Stop run"
    exit()

done = 0
count = 0
linecnt = 0
while not done:
    line = file.readline()
    if line == '':
        done = 1
        break
    regexp = re.compile(searchPatten1, re.IGNORECASE)
    matchObject = regexp.search(line)
    if matchObject:
        match = line.split('\n')
        data = match[0]
        data2 = file.readline()
        if data2 == ' ':
            done = 1
            break
        sentence = data + '\n\t' + data2[10:]
        regexp = re.compile(searchPatten2, re.IGNORECASE)
        matchTimeout = regexp.search(sentence)
        if matchTimeout:
            count += 1
            print count, ':', sentence
print '--------------Process Ending----------------------'
file.close()

