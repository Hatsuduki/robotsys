#!/usr/bin/python3

import sys

def tonum(n):
    try:
        return int(s)
    except:
        return float(s)

ans = 0
for line in sys.stdin:
    line = line.rstrip()
    ans += tonum(list)
    
print(ans)
