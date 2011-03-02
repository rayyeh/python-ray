#!/usr/bin/env python

import sys
import time
from nucular import Nucular

# create an instance.
session = Nucular.Nucular(sys.argv[1])
query = session.Query()
query.anyWord(sys.argv[2])
start = time.time()
d = query.resultDictionaries()
print "Query Duration: %f" % (time.time() - start)
print "Results: %d" % len(d)
