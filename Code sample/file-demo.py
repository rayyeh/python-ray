import linecache
filePath = "c:/input.txt"

print linecache.getline(filePath, 1)
print linecache.getline(filePath, 3)
linecache.clearcache()
