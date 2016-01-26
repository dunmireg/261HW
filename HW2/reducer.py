#!/usr/bin/python
import sys

# input comes from STDIN
for line in sys.stdin:

    # parse the input we got from mapper.py
    line = line.split('\t')
    count = line[0]
    word = line[1].rstrip()
    
    #reverse order, relying on hadoop shuffling to get into proper order
    print word + '\t' + count