from BeautifulSoup import BeautifulSoup
import requests

url = 'http://stefan.sofa-rockers.org/search/?q=%(q)s'
payload = {'q': 'Python',}
r = requests.get(url % payload)


soup = BeautifulSoup(r.text)
titles = [h2.text for h2 in soup.findAll('h2', attrs={'class': 'post_title'})]

for t in titles:
    print(t)
