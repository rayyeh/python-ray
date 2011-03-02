#!/usr/bin/python

import sys

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
        print >>sys.stderr, "Requires src and dst"
        sys.exit(-1)

    # Run Copy.
    chars = copy_utf8(*sys.argv[1:])
    print "%d chars copied" % chars
