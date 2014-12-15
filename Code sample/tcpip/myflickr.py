#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""An index of your flickr photos.
You need the module flickrapi from
http://flickrapi.sourceforge.net/"""
from builtins import object

# Add your API key below
API_KEY = ""
MY_USER_ID = '92383858@N00'
TEMPLATE = """
   %(pictures)s
 """

import flickrapi
import random


class FlickrIndex(object):
    """Makes a simple HTML index of your flickr photos."""

    def __init__(self,
                 api_key,
                 my_user_id='43827815@N00'):
        self.flickr = flickrapi.FlickrAPI(api_key)
        self.my_user_id = my_user_id
        self.sets = self.flickr.photosets_getList(user_id=self.my_user_id)

    def print_sets(self):
        """Makes an unordered list of sets."""

        setsection = "<h1>My Flickr Sets</h1> \n"
        setsection += "<ul> \n"
        for i in self.sets.photosets[0].photoset:
            setsection += '<li><a href="' + 'http://www.flickr.com/photos/' + \
                          self.my_user_id + '/sets/' + i['id'] + \
                          '">' + i.title[0].text + '</a></li> \n'
        setsection += "</ul>"
        return setsection

    def print_photos(self):
        """Makes an unordered list of pictures."""
        photos = self.flickr.photos_search(user_id=self.my_user_id)

        picsection = "<h1>My Flickr Photos</h1> \n"
        for i in photos.photos[0].photo:
            picsection += '<li><a href="' + 'http://www.flickr.com/photos/' + \
                          self.my_user_id + '/' + i['id'] + \
                          '">' + i['title'] + '</a></li> \n'
        picsection += "</ul> \n"
        return picsection

    def print_random_photos(self, photo_number=5):
        random_page = random.randint(1, 3300)
        photos = self.flickr.photos_search(user_id=self.my_user_id, per_page=photo_number, page=random_page)
        picsection = ""
        for i in photos.photos[0].photo:
            picsection += '<a href="http://www.flickr.com/%s/%s"><img src="http://farm%s.static.flickr.com/%s/%s_%s_m.jpg" /></a>   \n' % (
                self.my_user_id, i['id'], i['farm'], i['server'], i['id'], i['secret'])
        picsection += " \n"
        return picsection


def main():
    """Might as well try to do something if called directly"""
    webpage = FlickrIndex(API_KEY, MY_USER_ID)
    # includes = {'picsets': webpage.print_sets(), 'pictures' : webpage.print_random_photos(10) }
    includes = {'pictures': webpage.print_random_photos(15)}

    f = open('myflickr.html', 'w+')
    f.write(TEMPLATE % includes)
    f.close()

    import popen2

    opener = popen2.popen3('gnome-open ' + 'myflickr.html')

# start the ball rolling
if __name__ == "__main__":
    main()
    
