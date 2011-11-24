# -*- coding: utf-8 -*-
# parsing 經濟部工業局工廠公示資料查詢  資料

import urllib2
import re
from BeautifulSoup import BeautifulSoup
import string 


def getdata(id):
    #url="http://gcis.nat.gov.tw/Fidbweb/factInfoAction.do?method=detail&estbid=04263000001962&agencyCode=379100000G"

    url="http://gcis.nat.gov.tw/Fidbweb/factInfoAction.do?method=detail&estbid="+id+"&agencyCode=379100000G"
    print url

    YahooStock = urllib2.urlopen(url)
    StockContent = YahooStock.read().decode('cp950')
    soup=BeautifulSoup(StockContent)
    YahooStock.close()
    pTag=soup.p

    data=''
    allTags = soup.findAll(color="#66FFFF")
    for tag in allTags:
        textlist=[]
        textcontent=[]
        textcontent=tag.contents[0]
        textcontent=textcontent.replace('\t','')
        textcontent=textcontent.replace('\n','')
        textcontent=textcontent.replace(' ','')
        textcontent=textcontent.replace('\x0D','')
        textcontent=textcontent.replace('\x00','')        
        data=data+textcontent+';'
        
    if len(data) < 4:
        print 'wrong id'
    else:    
        allTags =soup.findAll(size="2")
        for tag in allTags:
            textlist=[]
            textcontent=[]
            textcontent=tag.contents[0]
            textcontent=textcontent.replace('\t','')
            textcontent=textcontent.replace('\n','')
            textcontent=textcontent.replace(' ','')
            textcontent=textcontent.replace('\x0D','')
            textcontent=textcontent.replace('\x00','')     
            data=data+textcontent+';'
    return data
        

if __name__ == "__main__":
    #filePath = "c:/input.txt"
    #file = open(filePath, 'w+')
    value =''
    
    value=getdata('04263000001943')
    print value
    #file.write(value)
    #file.close()
    