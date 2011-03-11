# -*- coding: utf-8 -*-

import urllib2
import re
from BeautifulSoup import BeautifulSoup

YahooStock = urllib2.urlopen("http://tw.stock.yahoo.com/q/q?s=1303")
StockContent = YahooStock.read().decode('cp950')
soup=BeautifulSoup(StockContent)
YahooStock.close()
#print StockContent

#print soup.prettify()

print soup.head.parent.name
pTag=soup.p
print pTag.contents
print '#######################'
print soup.b.string
print '#######################'
#print soup.body
print '####################'

stock=[]
#<a href="/q/bc?s=1303">1303南亞</a>
stockname=soup.find(href=re.compile("^\/q\/bc\?s"))
stock.append(stockname.text)

#<td align="center" bgcolor="#FFFfff" nowrap>14:30</td>

allTags = soup.findAll(nowrap="nowrap",bgcolor="#FFFfff")
for tag in allTags:
    stock.append(tag.text)
stockprint=(stock[0],stock[1])
print "名稱 :%s,時間 %s" %stockprint


