#!/usr/bin/python
import sys

#lines have format word + \t + count + \t + relative count
for line in sys.stdin:
    line = line.split('\t')
    print line[1] + '\t' + line[0] + '\t' + line[2]