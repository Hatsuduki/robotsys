#!/usr/bin/python3

import sys

minus = 0
zero = 0
plus = 0

for i in sys.argv[1:]:
    if float(i) < 0:
        minus += 1
    elif float(i) == 0:
        zero += 1
    elif float(i) > 0:
        plus += 1

print("minus: ",minus," zero: ",zero," plus: ",plus)
