import urllib2
from BeautifulSoup import BeautifulSoup

response = urllib2.urlopen('http://python.org/')
html = response.read()
soup = BeautifulSoup(html)
print soup.prettify()

