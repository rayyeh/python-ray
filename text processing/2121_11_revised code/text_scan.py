#!/usr/bin/env python

import os
import sys
import time
from optparse import OptionParser

class StringNotFoundError(Exception):
    """String was not found"""

def search_dir(dirpath, string):
    """Search a file for a string"""
    where = 0
    for base_dir, dirs, files in os.walk(dirpath):
        for f in files:
            open_path = os.path.join(base_dir, f)
            with open(open_path) as fhandle:
                for line in fhandle:
                    if string in line:
                        where += 1
                        return where, open_path
            
    # if we get here, it wasn't found.
    raise StringNotFoundError(
        "We didn't see %s at all" % string)

if __name__ == '__main__': 
    parser = OptionParser()
    parser.add_option('-H', '--haystack',
        help="Base directory to search")

    parser.add_option('-n', '--needle',
        help='What to look for')

    opts, args = parser.parse_args()
    if not opts.needle or not opts.haystack:
        parser.error('Needle and haystack required')

    try:
        start = time.time()
        line, path = search_dir(opts.haystack, opts.needle)
        print "String Found on line %d in file %s in %f seconds" % \
                (line, path, time.time() - start)
    except StringNotFoundError, e:
        print >>sys.stderr, str(e)
            
