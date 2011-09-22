# -*- coding: utf-8 -*-

import urllib2
import re
from BeautifulSoup import BeautifulSoup

stocknum='1303'
url="http://tw.stock.yahoo.com/q/q?s="+stocknum

YahooStock = urllib2.urlopen(url)
StockContent = YahooStock.read().decode('cp950')
soup=BeautifulSoup(StockContent)
YahooStock.close()

#列印所有html 內容
print soup.prettify()

print 'soup.head.parent.name:',soup.head.parent.name
pTag=soup.p
print 'pTag.contents:',pTag.contents
#print soup.b.string
print '#######################'
#print soup.body
print soup.NESTABLE_TAGS['tr']
stock=[]

# 找個 股票名稱 <a href="/q/bc?s=1303">1303南亞</a>
stockname=soup.find(href=re.compile("^\/q\/bc\?s"))
stock.append(stockname.text)

# 找個 股票買賣資訊
#<td align="center" bgcolor="#FFFfff" nowrap>14:30</td>
allTags = soup.findAll(nowrap="nowrap",bgcolor="#FFFfff")
for tag in allTags:
    stock.append(tag.text)

stockprint=(stock[0],stock[1],stock[2],stock[3],stock[4],stock[5],stock[6])
print "名稱 :%s,時間 %s,%s,%s,%s,%s,%s" %stockprint


