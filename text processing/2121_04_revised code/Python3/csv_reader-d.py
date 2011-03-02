import csv
import sys
import json
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-f', '--file', help="CSV Data File")
    opts, args = parser.parse_args()

    if not opts.file:
        parser.error('File name is required')

    csv.register_dialect('passwd', delimiter=':',
        quoting=csv.QUOTE_NONE)

    dict_keys = ('login', 'pwd', 'uid', 'gid', 
        'comment', 'home', 'shell')
    
    # Create a dict reader from an open file 
    # handle and iterate through rows.
    reader = csv.DictReader(
        open(opts.file, 'rU'), fieldnames=dict_keys, dialect='passwd')

    # Dump the contents
    json.dump(
        list(reader), sys.stdout,
            sort_keys=True, indent=4)
    
