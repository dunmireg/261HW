#!/usr/bin/python
#Credit to the test notebook provided by Professor Shanahan for structure of mapper and reducer
import sys
import re

WORD_RE = re.compile(r"[\w']+") #regex for matching to word
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #split line into subcomponents by tab, ID + spam flag + subject + content
    components = line.split('\t')
    text = components[2] + components[3] #combine subject and content
    # increase counters
    for word in WORD_RE.findall(text):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)