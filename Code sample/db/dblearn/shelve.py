# ##################################################
# ## Demo:Storing Objects in a Shelve File
# ####################################################
print '#' * 40
print 'Demo:Storing Objects in a Shelve File'
print '#' * 40

import shelve

flights = {"1144": "Dallas", "1045": "Los Angeles", \
           "1520": "New York"}
times = ["230pm", "320pm", "420pm"]

#Create shelve
db = shelve.open("shelved.dat", "n")

#Store objects in shelve
db['flights'] = flights
db['times'] = times

#Display added keys
print list(db.keys())

db.close()

#Display the file contents
f = open("shelved.dat", "r")
data = f.read()
print 'Display the file contents ' + data
f.close()

###################################################
### Demo:Retrieving Objects from a Shelve File
#####################################################
print '#' * 40
print 'Demo:Retrieving Objects from a Shelve File'
print '#' * 40

import shelve

#Open shelve file
db = shelve.open("shelved.dat", "r")

#Get the keys from the shelve
for k in list(db.keys()):
    obj = db[k]
    print "%s: %s" % (k, obj)

#Use keys to get values
flightDB = db['flights']
flights = list(flightDB.keys())
cities = list(flightDB.values())
times = db['times']

print "\nDepartures"
print "============================================="
x = 0
for flight in flights:
    print ("Flight %s leaves for %s at %s" % \
           (flight, cities[x], times[x]))
    x += 1

db.close()

###################################################
### Demo:Changing Objects in a Shelve File
#####################################################
print '#' * 40
print 'Demo:Changing Objects in a Shelve File'
print '#' * 40
import shelve

newtimes = ["110pm", "220pm", "300pm", "445pm"]

#Open shelve file
db = shelve.open("shelved.dat", "w", writeback=1)

#Get the keys
for k in list(db.keys()):
    obj = db[k]
    print "%s: %s" % (k, obj)

print "\n"
print 'DB data:'
print db

#Use keys to get values
flights = db['flights']
times = db['times']

print '#Use keys to get values'
print flights
print times

#Update contents of old object
del flights['1144']
flights['1145'] = "Dallas"
flights['1709'] = "Orlando"

#Replace old object with a new object
db['times'] = newtimes

#Add a new object
db['oldtimes'] = times

#Flush data to disk
db.sync()

for k in list(db.keys()):
    obj = db[k]
    print "%s: %s" % (k, obj)

print 'DB data:'
print db
db.close()


