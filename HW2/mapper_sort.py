#!/usr/bin/python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    word, count = line.split('\t') #split into components of word, count
    print '%s\t%s' % (count, word) #print result to STDOUT for input to reducer