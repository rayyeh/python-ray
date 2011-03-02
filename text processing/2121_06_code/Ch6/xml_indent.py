from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class IndentHandler(ContentHandler):
    def __init__(self, *args, **kw):
        ContentHandler.__init__(self, *args, **kw)
        self.indent = 0
        self._factor = 4
        self.elements = 0

    def startElement(self, name, attrs):
        """
        Called when an element is encountered.
        """
        if self.indent:
            print '-' * (self.indent * self._factor),
           
        print name, " (depth %d)" % self.indent
        self.elements += 1
        self.indent += 1

    def endElement(self, name):
        self.indent -= 1

# This enters the XML parsing loop
handler = IndentHandler()
parser = make_parser()
parser.setContentHandler(handler)
parser.parse(open('world00.xml'))
print "Total Elements: %d" % handler.elements
