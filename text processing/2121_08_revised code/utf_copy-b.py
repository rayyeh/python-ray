#!/usr/bin/python

import sys
from gettext import install

# Install the _ function and setup our locale
# directory. 
install('utf_copy', 'lang', unicode=True)

def copy_utf8(src, dst):
    """
    Copy a file.

    Copies a file and returns the number
    of characters that we've copied.
    """
    with open(dst, 'wb') as output:
        with open(src, 'r') as input:
            u = input.read().decode('utf-8')
        output.write(u.encode('utf-8'))
    return len(u)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print >>sys.stderr, _(u"Requires src and dst")
        sys.exit(-1)

    # Run Copy.
    chars = copy_utf8(*sys.argv[1:])

    # create this here, otherwise 'chars' will be
    # included in our gettext call.
    format_dict = {'chars': chars}
    
    # NOTE: The 'chars' value may be plural
    print _(u"%(chars)d chars copied") % format_dict
