import sys
import re

# Make sure we have a single URL argument.
if len(sys.argv) != 2:
    print("URL Required", file=sys.stderr)
    sys.exit(-1)

# Easier access.
url = sys.argv[1]

# Ensure we were passed a somewhat valid URL.
# This is a superficial test.
if re.match(r'^https?:/{2}\w.+$', url):
    print("This looks valid")
else:
    print("This looks invalid")

    


