#################################################
print '#' *50
print '#Demo:Retrieving Text from HTML Documents'
print '#' *50

import HTMLParser
import urllib

urlText = []

#Define HTML Parser
class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)


#Create instance of HTML parser
lParser = parseText()

#Feed HTML file into parser
lParser.feed(urllib.urlopen("http://python.org/").read())

lParser.close()

print 'urlTest',urlText

for item in urlText:
    print item
