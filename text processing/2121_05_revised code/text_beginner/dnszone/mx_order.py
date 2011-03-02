import re
import optparse
from collections import namedtuple

# Two differnet lines to make for 
# easier fomatting.
ttl_re = r'^(\$TTL\s+(?P<ttl>\d+).*)$'
mx_re = r'^((?P<dom>@|[\w.]+))?\s+(?P<dttl>\d+)?.*MX\s+(?P<wt>\d+)\s+(?P<tgt>.+).*$'

# This makes it easier to reference our values and
# makes code more readable.
MxRecord = namedtuple('MxRecord', 'wt, dom, dttl, tgt')

# Compile it up. We'll accept either 
# one of the above expressions.
zone_re = re.compile('%s|%s' % (ttl_re, mx_re), 
    re.MULTILINE | re.IGNORECASE)

def zoneify(zone, record):
    """
    Format the record correctly.
    """
    if not record or record == '@':
       record =  zone + '.'
    elif not record.endswith('.'):
        record = record + '.%s.' % zone
    return record

def parse_zone(zone, text):
    """
    Parse a zone for MX records.
    
    Iterates through a zone file and pulls
    out relevent information.
    """
    ttl = None
    records = []
    for match in zone_re.finditer(open(text).read()):
        ngrps = match.groupdict()
        if ngrps['ttl']:
            ttl = ngrps['ttl']
        else:
            dom = zoneify(zone, ngrps['dom'])
            dttl = ngrps['dttl'] or ttl
            tgt = zoneify(zone, ngrps['tgt'])
            wt = int(ngrps['wt'])
    
            records.append(
                MxRecord(wt, dom, dttl, tgt))
           
    return sorted(records)

def main(arg_list=None):
    parser = optparse.OptionParser()
    parser.add_option('-z', '--zone', help="Zone Name")
    parser.add_option('-f', '--file', help="Zone File")
    opts, args = parser.parse_args()
    if not opts.zone or not opts.file:
        parser.error("zone and file required")

    results = parse_zone(opts.zone, opts.file)
    print "Mail eXchangers in preference order:"
    print
    for mx in results:
        print "%s %6s %4d %s" % \
            (mx.dom, mx.dttl, mx.wt, mx.tgt)


