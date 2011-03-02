import sys
from HTMLParser import HTMLParser
from urllib2 import urlopen

class LinkDetect(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            try:
                print dict(attrs)['href']
            except KeyError: 
                pass

def check_page(url):
    link_finder = LinkDetect()
    file_obj = urlopen(url)
    for line in file_obj:
        link_finder.feed(line)
    link_finder.close()

if __name__ == '__main__':
    check_page(sys.argv[1])
