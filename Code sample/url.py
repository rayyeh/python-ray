print '#' * 50
print '#Demo:Parsing URLs'
print '#' * 50

import urlparse

URLscheme = "http"
URLlocation = "www.python.org"
URLpath = "lib/module-urlparse.html"

modList = ("urllib", "urllib2","httplib", "cgilib")

#Parse address into tuple
print "Parsed Google search for urlparse"
parsedTuple = urlparse.urlparse("http://www.google.com/search?hl=en&q=urlparse&btnG=Google+Search")
print parsedTuple

#Unparse list into URL
print "\nUnarsed python document page"
unparsedURL = urlparse.urlunparse( \
(URLscheme, URLlocation, URLpath, '', '', ''))
print "\t" + unparsedURL

#Join path to new file to create new URL
print "\nAdditional python document pages using join"
for mod in modList:
    newURL = urlparse.urljoin(unparsedURL, \
                    "module-%s.html" % (mod))
    print "\t" + newURL

#Join path to subpath to create new URL
print "\nPython document pages using join of sub-path"
newURL = urlparse.urljoin(unparsedURL,
         "module-urllib2/request-objects.html")
print "\t" + newURL

#####################################################################
print '#' * 50
print '#Demo:Opening HTML Documents'
print '#' * 50
import urllib

webURL = "http://www.yahoo.com.tw"
#localURL = "/books/python/CH8/code/test.html"

#Open web-based URL
u = urllib.urlopen(webURL)
buffer = u.read()
print u.info()
print "Read %d bytes from %s.\n" % \
(len(buffer), u.geturl())

#Open local-based URL
#u = urllib.urlopen(localURL)
#buffer = u.read()
#print u.info()
#print "Read %d bytes from %s." % \
#(len(buffer), u.geturl())


