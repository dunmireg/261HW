#!/usr/bin/python
import sys

#Structure is word + \t + count + \t + relative count, to be read from output of first set of jobs

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t') #split the line
    print line[1] + '\t'+ line[0] + '\t' + line[2] #now we are using the number as the key, this will be sorted