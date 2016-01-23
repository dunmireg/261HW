#!/usr/bin/python
import sys

# input comes from STDIN
for line in sys.stdin:

    # parse the input we got from mapper.py
    count, word = line.split('\t')
    
    print word + ', ' + count