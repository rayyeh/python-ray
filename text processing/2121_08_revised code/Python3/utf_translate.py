#!/usr/bin/python3

import codecs
import sys

from optparse import OptionParser

def rewrite(src, dst, encoding):
    """
    Read a UTF-8 Stream and rewrite.

    Reads a UTF-8 stream from standard
    in and rewrites it as dst with the
    target encoding.
    """
    with open(src, 'r', encoding='utf-8') as input:
        with open(dst, 'w', encoding=encoding) as output:
            for line in input:
                output.write(line)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-s', '--source', 
        help='File to read from')
    parser.add_option('-d', '--destination',
        help='Target file for copy')
    parser.add_option('-e', '--encoding',
        help='Destionation Encoding')

    opts, args = parser.parse_args()

    # check count
    if not opts.destination \
            or not opts.encoding or not opts.source:
        parser.error('options missing')

    # check valid encoding
    try:
        codecs.lookup(opts.encoding)
    except LookupError as e:
        parser.error(str(e))

    # Do the work
    rewrite(opts.source,
        opts.destination, opts.encoding)
