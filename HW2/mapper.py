#!/usr/bin/python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    components = line.split('\t')
    #reverse input, so instead of word, count it now becomes count, word with count serving as key
    #note convert number to an int to remove new line character, then turn to string
    print components[1].rstrip() + '\t' + components[0] #print result to STDOUT for input to reducer