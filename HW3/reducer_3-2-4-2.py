#!/usr/bin/python
import sys

current_word = None
current_count = None
word = None
word_count = {}

for line in sys.stdin:
    line = line.split('\t')
    #recall format is count + \t + word + \t relative count
    count = line[0]
    word = line[1]
    rel_count = line[2]
    print word + '\t' + count + '\t' + rel_count
    
    