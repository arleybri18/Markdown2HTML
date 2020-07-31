#!/usr/bin/python3

import sys
import os.path

if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
else:
    if os.path.isfile('./' + sys.argv[1]):
        sys.exit()
    else:
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

