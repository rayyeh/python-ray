import simplejson
import urllib
#import json

APP_ID = 'YahooDemo' # Change this to your API key
SEARCH_BASE = 'http://search.yahooapis.com/WebSearchService/V1/webSearch'

class YahooSearchError(Exception):
    pass

def search(query, results=10, start=1, **kwargs):
    kwargs.update({
        'appid': APP_ID,
        'query': query,
        'results': results,
        'start': start,
        'output': 'json'
    })
    url = SEARCH_BASE + '?' + urllib.urlencode(kwargs)
    result = simplejson.load(urllib.urlopen(url))
    if 'Error' in result:
        # An error occurred; raise an exception
        raise YahooSearchError, result['Error']
    return result['ResultSet']

search_string=raw_input('Enter your search word:')
info = search(search_string)
#info['totalResultsReturned']
results = info['Result']
for result in results:
    print 'Title:',result['Title'],'\n','  Result:', result['Url'],\
          '\n','  Summary:',result['Summary']


