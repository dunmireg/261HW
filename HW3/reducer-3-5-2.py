#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.split('\t')
    #structure currently is count + word + relative count
    print line[1] + '\t' + line[0] + '\t'+ line[2]