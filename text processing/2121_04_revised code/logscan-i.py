#!/usr/bin/python

import os
import time
import string
import sys
from optparse import OptionParser
from collections import defaultdict
from ConfigParser import SafeConfigParser
from ConfigParser import ParsingError

class LogProcessor(object):
    """
    Process a combined log format.

    This processor handles log files in a combined format, 
    objects that act on the results are passed in to 
    the init method as a series of methods.
    """
    tmpl = string.Template(
        'line $line is malformed, raised $exc error: $error')

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
            'file_requested': parts[6],
            'status': parts[8]
        }

    def report(self):
        """
        Run report chain.
        """
        for c in self._call_chain:
            print c.title
            print '=' * len(c.title)
            c.report()
            print

    def parse(self, handle):
        """
        Parses the log file.

        Returns a dictionary composed of log entry values, 
        for easy data summation.
        """
        line_count = 0
        for line in handle:
            line_count += 1
            try:
                fields = self.split(line)
            except Exception, e:
                print >>sys.stderr, self.tmpl.substitute(
                        line=line_count, 
                        exc=e.__class__.__name__, 
                        error=e)
                continue
            for handler in self._call_chain:
                getattr(handler, 'process')(fields)

        return line_count

class ErrorCodeHandler(object):
    """
    Collect Error Code Information.
    """
    title = 'Error Code Breakdown'

    def __init__(self):
        self.error_codes = defaultdict(int)
        self.errors = 0
        self.lines = 0

    def process(self, fields):
        """
        Scan each line's data.

        Reading each line in, we'll save out the 
        number of response codes we run into so we 
        can get a picture of our success rate.
        """
        code = fields['status']
        self.error_codes[code] += 1

        # Assume anything > 400 is
        # an HTTP error
        self.lines += 1
        if int(code) >= 400:
            self.errors += 1

    def report(self):
        """
        Print out Status Summary.

        Create the status segment of the
        report.
        """
        longest_num = sorted(self.error_codes.values())[-1]
        longest = len(str(longest_num))

        for k,v in self.error_codes.items():
            print '{0}: {1:>{2}}'.format(k, v, longest)

        # Print summary information
        print 'Errors: {0}; Failure Rate: {1:%}; Codes: {2}'.format(
            self.errors, float(self.errors)/self.lines,
                len(self.error_codes.keys()))
    
class MaxSizeHandler(object):
    """
    Check a file's size.
    """
    def __init__(self, size):
        self.size = size
        self.name_size = 0
        self.warning_files = set()

    @property
    def title(self):
        return 'Files over %d bytes' % self.size

    def process(self, fields):
        """
        Looks at each line individually.

        Looks at each parsed log line individually and 
        performs a size calculation. If it's bigger than 
        our self.size, we just print a warning.
        """
        if fields['size'] > self.size:
            self.warning_files.add(
                (fields['file_requested'], fields['size']))
    
            # We want to keep track of the longest file 
            # name, for formatting later.
            fs = len(fields['file_requested'])
            if fs > self.name_size:
                self.name_size = fs
               
    def report(self):
        """
        Format the Max Size Report.

        This method formats the report and prints 
        it to the console.
        """
        for f,s in self.warning_files:
            print '%-*s :%d' % (self.name_size, f, s)

def load_config():
    """
    Load configuration.

    Reads the name of the configuration 
    of of sys.argv and loads our config.
    from disk.
    """
    parser = OptionParser()
    parser.add_option('-c', '--config', dest='config',
        help="Configuration File Path")

    opts, args = parser.parse_args()
    if not opts.config:
        parser.error('Configuration File Required')
        
    # Build config parser and set some
    # reasonable defaults.
    config_parser = SafeConfigParser(
        defaults={
            'input_source': '-',
            'dir': os.getcwd(),
            'threshold': '0',
            'show_footer': 'True'
        }
    )

    if not config_parser.read(opts.config):
        parser.error('Could not parse configuration')

    return config_parser

if __name__ == '__main__':

    config = load_config()

    input_source = config.get('main', 'input_source')
    if input_source == '-':
        file_stream = sys.stdin
    else:
        try:
            file_stream = open(input_source)
        except IOError, e:
            print >>sys.stderr, str(e)
            sys.exit(-1)

    size_check = MaxSizeHandler(
        int(config.get(
            'maxsize', 'threshold')
        )
    )
    call_chain = []
    call_chain.append(size_check)
    call_chain.append(ErrorCodeHandler())
    processor = LogProcessor(call_chain)

    initial = time.time()
    line_count = processor.parse(file_stream)
    duration = time.time() - initial

    # Ask the processor to display the
    # individual reports.
    processor.report()

    if config.getboolean('display', 'show_footer'):
        # Print our internal statistics
        print "Report Complete!"
        print "Elapsed Time: %#.8f seconds" % duration
        print "Lines Processed: %d" % line_count 
        print "Avg. Duration per line: %#.16f seconds" % \
            (duration / line_count) if line_count else 0
