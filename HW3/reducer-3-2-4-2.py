#!/usr/bin/python
import sys

print "Issue" + '\t' + "Count" + '\t' + 'Relative Count'
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    #structure currently is count + word + relative count
    print line[1] + '\t' + line[0] + '\t'+ line[2]