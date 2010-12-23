import lxml.html
from lxml.html import fromstring
import urllib
import re
links = lxml.html.parse("http://www.python.org/").xpath("//a/@href") 
#for link in links: 
#    print link 

url="http://www.python.org"
content=urllib.urlopen(url).read()
doc=fromstring(content)
doc.make_links_absolute(url)
print doc.text_content()

#for el in doc.find_class_name('highlight'):
#    print el