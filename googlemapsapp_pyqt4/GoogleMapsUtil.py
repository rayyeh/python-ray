import urllib

GMap_KEY_ID = 'ABQIAAAApIB1Ubv-TkAKBJ37W0Hh2RS1AC4DxUbsxJ-9A5H8anlW8PhTrBQW71UJo3SK1Lm1LK_DZxfeCJessA'

def getGMapsGEO(qaddr):
     geo_url = 'http://maps.google.com/maps/geo?'+urllib.urlencode({'q':qaddr})+'&output=csv&key='+GMap_KEY_ID
     gdata = urllib.urlopen(geo_url)
     gdataArray = gdata.read().split(',') 
     return gdataArray

def getGMapsStaticUrl(Latitudes, Longitudes, zoom=14, width=512, height=512):
     #print "--"+str(Latitudes)+"--"+str(Longitudes)+"--"+str(zoom)
     map_url = 'http://maps.google.com/staticmap?center='+str(Latitudes)+','+str(Longitudes)+'&zoom='+str(zoom)+\
         '&size='+str(width)+'x'+str(height)+'&maptype=mobile&key='+GMap_KEY_ID+'&sensor=false'
     return map_url
