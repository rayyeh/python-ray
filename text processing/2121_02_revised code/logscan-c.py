#!/usr/bin/python

import sys
from optparse import OptionParser

class LogProcessor(object):
    """
    Process a combined log format.

    This processor handles log files in a combined format, 
    objects that act on the results are passed in to 
    the init method as a series of methods.
    """
    def __init__(self, call_chain=None):
        """
        Setup parser.

        Save the call chain. Each time we process a log,
        we'll run the list of callbacks with the processed
        log results.
        """
        if call_chain is None:
            call_chain = []
        self._call_chain = call_chain

    def split(self, line):
        """
        Split a log file.

        Initially we just want size and requested file name, so
        we'll split on spaces and pull the data out. 
        """
        parts = line.split()
        return {
            'size': 0 if parts[9] == '-' else int(parts[9]), 
            'file_requested': parts[6]
        }

    def parse(self, handle):
        """
        Parses the log file.

        Returns a dictionary composed of log entry values, 
        for easy data summation.
        """
        for line in handle:
            fields = self.split(line)
            for func in self._call_chain:
                func(fields)

class MaxSizeHandler(object):
    """
    Check a file's size.
    """
    def __init__(self, size):
        self.size = size

    def process(self, fields):
        """
        Looks at each line individually.

        Looks at each parsed log line individually and 
        performs a size calculation. If it's bigger than 
        our self.size, we just print a warning.
        """
        if fields['size'] > self.size:
            print >>sys.stderr, \
                'Warning: %s exceeeds %d bytes (%d)!' % \
                    (fields['file_requested'], self.size,
                      fields['size'])

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-s', '--size', dest="size",
        help="Maximum File Size Allowed", 
            default=0, type="int")

    parser.add_option('-f', '--file', dest="file",
        help="Path to Web Log File", default="-")
           
    opts,args = parser.parse_args()
    call_chain = []
  
    if opts.file == '-':
        file_stream = sys.stdin
    else:
        try:
            file_stream = open(opts.file)
        except IOError, e:
            print >>sys.stderr, str(e)
            sys.exit(-1)

    size_check = MaxSizeHandler(opts.size)
    call_chain.append(size_check.process)
    processor = LogProcessor(call_chain)
    processor.parse(file_stream)


