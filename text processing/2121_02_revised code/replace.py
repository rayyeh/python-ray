import sys
import fileinput

# Iterate through all lines and replace
# convert everything to upper case.
for line in fileinput.input(inplace=1, backup='.bak'):
    sys.stdout.write(line.upper())
    
