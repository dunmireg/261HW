#!/usr/bin/python
import sys

current_word = None
current_count = None
word = None

for line in sys.stdin:
    #issue, count = line.split('\t')
    line = line.split('\t')
    word = line[0]
    count = int(line[1])
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            #sys.stderr.write('reporter:counter:Reduce-Counter,Total,1\n')
            print '%s\t%s' % (current_word, current_count)
        current_word = word
        current_count = count

if current_word == word:
    #sys.stderr.write('reporter:counter:Reduce-Counter,Total,1\n')
    print '%s\t%s' % (current_word, current_count)