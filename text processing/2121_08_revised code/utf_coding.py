#!/usr/bin/python

with open('russian.txt', 'r') as ru:
    txt = ru.read()

# Bytes Read
print "Bytes: %d" % len(txt)

# First, we'll decode.
uc = txt.decode('utf-8')

# Chars after decode
print "Chars: %d" % len(uc)

