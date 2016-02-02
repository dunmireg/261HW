#!/usr/bin/python
import sys

print "Pair" + '\t' + "Count" + '\t' + 'Relative Count'
for line in sys.stdin:
    line = line.split('\t')
    print line
    #structure currently is count + word + relative count
    print line[1] + '\t' + line[0] + '\t'+ line[2]