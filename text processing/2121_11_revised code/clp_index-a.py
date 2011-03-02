#!/usr/bin/env python

import os
import email

from optparse import OptionParser
from nucular import Nucular

class IndexDirectory(object):
    def __init__(self, session, where, persist_every=100):
        self.where = where
        self.persist_every = persist_every
        self.session = session

    def index(self):
        for c,i in enumerate(os.listdir(self.where)):
            full_path = os.path.join(self.where, i)
            session.indexDictionary(
                full_path, self.build_dict(full_path))

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
    def build_dict(self, full_path):
        return { 'full_text':  open(full_path).read()}


class MessageIndex(IndexDirectory):
    def build_dict(self, full_path):
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
        
    
