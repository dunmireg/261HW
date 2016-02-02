#!/usr/bin/python
import sys

totalBaskets = 0
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    totalBaskets += 1
    
    for item in line:
        counts = {}
        for othItem in line:
            if othItem != item:
                if othItem in counts.keys():
                    counts[othItem] += 1
                else:
                    counts[othItem] = 1
        print item + '\t' + str(counts)
print "*" + '\t' + str(totalBaskets)