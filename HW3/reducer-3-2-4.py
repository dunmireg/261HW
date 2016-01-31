#!/usr/bin/python
import sys

current_word = None
current_count = None
word = None
total = 0

for line in sys.stdin:
    line = line.split('\t')
    word = line[0]
    count = int(line[1])
    if word == '*':
        total = count
    else:
        if current_word == word:
            current_count += count
        else:
            if current_word:
                #sys.stderr.write('reporter:counter:Reduce-Counter,Total,1\n')
                print '%s\t%s\t%s' % (current_word, current_count, float(current_count)/total)
            current_word = word
            current_count = count

if current_word == word:
    #sys.stderr.write('reporter:counter:Reduce-Counter,Total,1\n')
    print '%s\t%s\t%s' % (current_word, current_count, float(current_count)/total)