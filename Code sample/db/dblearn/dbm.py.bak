import anydbm

cities = ["Dallas", "Los Angeles", "New York"]
flights = ["1144", "1045", "1520"]
times = ["230pm", "320pm", "420pm"]

# Create DBM file
cityDB = anydbm.open("city.dbm", 'n')
timeDB = anydbm.open("time.dbm", 'n')

# Add entries
i = 0
for flight in flights:
    cityDB[flight] = cities[i]  # d[key] = value
    i += 1
i = 0
for flight in flights:
    timeDB[flight] = times[i]
    i += 1

print cityDB.items()
print timeDB.items()

# Close DBM file
cityDB.close()
timeDB.close()

##############################################
##Retrieving Entries from a DBM File
##############################################
import anydbm

#Open DBM file for reading
cityDB = anydbm.open("city.dbm", 'r')
timeDB = anydbm.open("time.dbm", 'r')

#Get keys
flights = cityDB.keys()

#Use keys to get values
print "Arrivals"
print
"============================================="
for flight in flights:
    print ("Flight %s arrives from %s at %s" %
           (flight, cityDB[flight], timeDB[flight]))

#Close DBM file
cityDB.close()
timeDB.close()

#####################################################
### Demo:Updating Entries in a DBM File
#####################################################
print '#' * 40
print 'Demo:Updating Entries in a DBM File'
print '#' * 40
import anydbm

flights = []
cancelled = ["1520", "1544"]
deleted = ["1144"]


def displayArrivals(header):
    print header
    print "========================================"
    for flight in flights:
        print ("Flight %s from %s arrives at %s" %
               (flight, cityDB[flight],
                timeDB[flight]))

#Open DBM file for reading
cityDB = anydbm.open("city.dbm", 'w')
timeDB = anydbm.open("time.dbm", 'w')

#Get keys
flights = timeDB.keys()

#Display arrivals
displayArrivals("Arrivals")

#Update DBM
for flight in flights:
    for c in cancelled:
        if c == flight:
            timeDB[flight] = "CANCELLED"
            break
    for d in deleted:
        if d == flight:
            del timeDB[flight]
            del cityDB[flight]
            break

#Display updataed arrivals
flights = timeDB.keys()
displayArrivals("Updated Arrivals")

#Close DMB file
cityDB.close()
timeDB.close()

#####################################################
### Demo:Pickling Objects to a File
#####################################################
print '#' * 40
print 'Demo:Pickling Objects to a File'
print '#' * 40

import anydbm
import cPickle

flights = {"1144": "Dallas", "1045": "Los Angeles", \
           "1520": "New York"}
times = ["230pm", "320pm", "420pm"]

#Create the pickle file
f = open("pickled.dat", "w")

#Create the pickler object
p = cPickle.Pickler(f)

#Pickle data to the file
p.dump(flights)
p.dump(times)
f.close()

#Display the file contents
f = open("pickled.dat", "r")
data = f.read()
print data
f.close()

###################################################
### Demo:Unpickling Objects from a File
#####################################################
print '#' * 40
print 'Demo:Unpickling Objects from a File'
print '#' * 40

import cPickle

#Open the pickle file
f = open("pickled.dat", "r")

#Create the unpickler object
p = cPickle.Unpickler(f)

#Unpickle an object from the file
data = p.load()
print "Flight Dictionary:"
print data

#Unpickle an object from the file
data = p.load()
print "\nTime List:"
print data

f.close()
###################################################
### Demo:Storing Objects in a Shelve File
#####################################################
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
print db.keys()

db.close()

#Display the file contents
f = open("shelved.dat", "r")
data = f.read()
print 'Display the file contents ' + data
f.close()
###################################################
### Demo:Storing Objects in a Shelve File
#####################################################
print '#' * 40
print 'Demo:Storing Objects in a Shelve File'
print '#' * 40


