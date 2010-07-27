year = {1:'January', 2:'February', 3:'March',4:'April',\
        5:'May', 6:'June', 7:'July', 8:'August',\
        9:'September', 10:'October', 11:'November',\
        12:'December'}

print year

#Get list of keys
months = year.keys()

#Create subset of keys
months.sort()
halfCount = len(months)/2
half = months[0:halfCount]
print 'month:'
print months

#Create new dictionary from subset of keys
firstHalf = {}
for x in half:
        firstHalf[x] = year[x]

print firstHalf


myDictionary = {'color':'blue', 'speed':'fast',
 'number':1, 5:'number'}

print myDictionary

#Swap keys for values
swap={}
for key,val in myDictionary.iteritems():
    swap[val]=key

print swap

