#!/usr/bin/python
import sys

for line in sys.stdin: #reads result of second mapper using number as key
    line = line.strip()
    line = line.split('\t')
    #structure currently is count + word + relative count
    print line[1] + '\t' + line[0] + '\t'+ line[2] #now reverse back to display word + count + relative count