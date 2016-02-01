#!/usr/bin/python
import sys

total = 0
line_num = 1
for line in sys.stdin:
    line = line.strip()
    items = line.split()
    for item in items:
        total += 1
        print item + '\t' + str(1)
    print '*' + '\t' + str(line_num) + '\t' + str(len(items))
    line_num += 1
print '*' + '\t' + str(0) + '\t' + str(total)