#!/usr/bin/env python

import tempfile
import datetime
import sys
import os
from mako.lookup import TemplateLookup

finder = TemplateLookup(
    os.path.join(os.getcwd(), 'templates'), 
    os.path.join(tempfile.gettempdir(), 'mako_cache'),
        output_encoding='utf=8', input_encoding='utf-8')

def render_email(email, 
    name, amount, date, products, template='thank_you.txt'):
    """
    Render an email message.

    Given the needed parameters, we'll render an email 
    message and return as a string.
    """
    tmpl = finder.get_template(template)
    return tmpl.render(
        email=email, name=name, amount=amount, 
            date=date, packing_list=products)

if __name__ == '__main__':
    # Some Fake Products
    products = []
    products.append(
        {'name': 'Whompster', 
         'quantity': 2, 
         'used': False,
         'descr': 'A high-quality Whomper'
         }
     )
    products.append(
        {'name': 'Blazooper', 
         'quantity': 1, 
         'used': True,
         'descr': 'Zoops at Blazing Speed'
         }
     )

    # Standard Shipping is 3 days.
    ships_on = datetime.datetime.now() + datetime.timedelta(days=3)

    print render_email('joe@customer.com', 
        'Joe Customer', 151.24, ships_on, products, sys.argv[1])
