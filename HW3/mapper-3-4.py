#!/usr/bin/python
import sys
from itertools import combinations

totalBaskets = 0
for line in sys.stdin:
    totalBaskets += 1
    line = line.strip()
    line = line.split()
    
    pairs = list(combinations(line, 2))
    for pair in pairs:
        pair = sorted(list(pair))
        print pair[0] + ' ' + pair[1] + '\t' + str(1)
print '*' + '\t' + str(totalBaskets)