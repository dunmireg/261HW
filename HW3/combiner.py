#!/usr/bin/python
import sys

current_word = None
current_count = None
word = None
sys.stderr.write('reporter:counter:Combiner-Counter,Total,1\n')
for line in sys.stdin:
    #issue, count = line.split('\t')
    line = line.split('\t')
    word = line[0]
    count = int(line[1])
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_word = word
        current_count = count

if current_word == word:
    print '%s\t%s' % (current_word, current_count)