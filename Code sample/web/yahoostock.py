# -*- coding: utf-8 -*-

import urllib2

YahooStock = urllib2.urlopen("http://tw.stock.yahoo.com/q/q?s=1303")
StockContent = YahooStock.read().decode('cp950')
YahooStock.close()
#print StockContent

import HTMLParser

# 用來解析台中地區天氣資訊的解析器，繼承自HTMLParser
class StockHTMLParser(HTMLParser.HTMLParser):
    '''def handle_starttag(self, tag, attrs):
        print u'標籤 %s %s 開始' % (tag, attrs)'''
        
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
           for name,value in attrs:
                if name == 'href'  and value =="/pf/pfsel?stocklist=1303;" :
                    print '@@',self.get_starttag_text()
                    attrs='stop'
    
    def handle_startendtag(self, tag, attrs):
        print u'空標籤 %s %s' % (tag, attrs)

    def handle_endtag(self, tag):
        print u'標籤 %s 結束' % tag

    def handle_data(self, data):
        print u'資料 "%s"' % data

    def handle_comment(self, data):
        print u'註解 "%s"' % data

    def unknown_decl(self, data):
        """Override unknown handle method to avoid exception"""
        pass

Parser = StockHTMLParser()

try:
    # 將網頁內容拆成一行一行餵給Parser
    for line in StockContent.splitlines():
        # 如果出現停止旗標，停止餵食資料，並且跳出迴圈
        if hasattr(Parser, 'stop') and Parser.stop:
            break
        Parser.feed(line)
except HTMLParser.HTMLParseError, data:
    print "# Parser error : " + data.msg

Parser.close()

print "Press enter to continue."
raw_input()
