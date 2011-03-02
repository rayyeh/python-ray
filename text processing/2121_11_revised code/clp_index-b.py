#!/usr/bin/env python

import os
import sys
import email
from odf import opendocument

from optparse import OptionParser
from nucular import Nucular

class NotIndexFriendly(Exception):
    """Given Indexer Won't Support Format"""

class IndexDirectory(object):
    def __init__(self, session, where, persist_every=100):
        self.where = where
        self.persist_every = persist_every
        self.session = session

    def index(self):
        for c,i in enumerate(os.listdir(self.where)):
            full_path = os.path.join(self.where, i)
            try:
                index_target = self.build_dict(full_path)
            except NotIndexFriendly, e:
                print >>sys.stderr, "we cannot index %s: %s" % \
                    (full_path, str(e))
                continue

            session.indexDictionary(full_path, index_target)
            
            session.store(lazy=True)
            if not c % self.persist_every:
                session.aggregateRecent(verbose=False, fast=True)

        # Run a final aggregation.
        session.aggregateRecent(verbose=False)
        session.moveTransientToBase()
        session.cleanUp()

    def build_dict(self, full_path):
        raise NotImplementedError("I'm abstract")


class FullTextIndex(IndexDirectory):
    def load_text(self, path):
        return open(path).read()

    def _walk_odf(self, element, text=None):
        if text is None:
            text = []
        if element.nodeType == element.TEXT_NODE:
            text.append(element.data)

        for child in element.childNodes:
            self._walk_odf(child, text)
        return ''.join(text)

    def load_odt(self, path):
        return self._walk_odf(
            opendocument.load(path).body)
        
    def build_dict(self, full_path):
        dispatch = {'.txt': self.load_text,
            '.odt': self.load_odt}

        # Pull a reader from our dispatch table,
        # or none.
        reader = dispatch.get(
            os.path.splitext(full_path)[-1], None)

        if not reader:
            raise NotIndexFriendly("Not Indexable Type: %s" % full_path)
       
        # Return a full text mesg.
        return { 'full_text':  reader(full_path)}


class MessageIndex(IndexDirectory):
    def build_dict(self, full_path):
        if not full_path.endswith('.txt'):
            raise NotIndexFriendly("Only Text Messages Supported")

        msg = email.message_from_file(open(full_path))
        indexable = dict(msg)
        indexable['Payload'] = msg.get_payload()
        return indexable

_dispatch_table = {'fulltext': FullTextIndex,
    'message': MessageIndex}

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-a', '--archive',
        help="Nucular Index Directory", default="nuke")

    parser.add_option('-p', '--path',
        help='Base Directory. All files indexed')

    parser.add_option('-i', '--init',
        help="Initialize Database", action="store_true",
            default=False)

    parser.add_option('-t', '--type',
        help="Index Type",
            choices=_dispatch_table.keys())

    opts, args = parser.parse_args()
    if not opts.path or not opts.type:
        parser.error("path and type are required")

    # create an instance.
    session = Nucular.Nucular(opts.archive)
    if opts.init:
        session.create()

    # Call correct class.
    _dispatch_table[opts.type](session, opts.path).index()
        
    
