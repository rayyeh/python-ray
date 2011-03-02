#!/usr/bin/env python

import os
from optparse import OptionParser
from nucular import Nucular

def index_contents(session, where, persist_every=100):
    """Index a directory at a time."""
    for c, i in enumerate(os.listdir(where)):
        full_path = os.path.join(where, i)
        print 'indexing %s' % full_path
        session.indexDictionary(
            full_path, {'full_text': open(full_path).read()})

        # Save it out
        session.store(lazy=True)
        if not c % persist_every:
            print "Aggregating..."
            session.aggregateRecent(verbose=False, fast=True)


    print "Final Aggregation..."
    session.aggregateRecent(verbose=False, fast=True)
    session.moveTransientToBase()
    session.cleanUp()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-a', '--archive',
        help="Nucular Index Directory", default="nuke")

    parser.add_option('-p', '--path',
        help='Base Directory. All files indexed')

    parser.add_option('-i', '--init',
        help="Initialize Database", action="store_true",
            default=False)

    opts, args = parser.parse_args()
    if not opts.path:
        parser.error("path is required")

    # create an instance.
    session = Nucular.Nucular(opts.archive)
    if opts.init:
        session.create()
   
    index_contents(session, opts.path)
