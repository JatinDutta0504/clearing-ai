#!/usr/bin/env python3
import sys

html = open('/dev/stdin').read()
open(sys.argv[1], 'w').write(html)
print(f"Wrote {len(html)} bytes to {sys.argv[1]}")
