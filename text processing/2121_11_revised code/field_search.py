#!/usr/bin/env python

from optparse import OptionParser
from nucular import Nucular

MAX_WORDSPACE = 5

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-a', '--archive',
        help="Nucular Index Directory", default="nuke")

    parser.add_option('-s', '--subject',
        help="Search subjects for this word")

    parser.add_option('-p', '--proximate',
        help="A proximate search. These words"
             "must be within %d words. Comma Sep." % MAX_WORDSPACE)

    opts, args = parser.parse_args()
    if not opts.subject or not opts.proximate:
        parser.error('subject and word list required')

    # create an instance.
    session = Nucular.Nucular(opts.archive)
    query = session.Query()

    query.attributeWord('Subject', opts.subject)
    query.proximateWords(
        opts.proximate.split(','), MAX_WORDSPACE)

    for d in query.resultDictionaries():
        print '%(i)s: Subject [%(Subject)s]"' % d


