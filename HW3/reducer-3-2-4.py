#!/usr/bin/python
import sys
import operator

current_word = None
current_count = None
word = None
total = 0
wordcount = {}

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
                #wordcount[current_word] = current_count
                print current_word + '\t' + str(current_count) + '\t' + str(float(current_count)/total)
            current_word = word
            current_count = count

if current_word == word:
    #sys.stderr.write('reporter:counter:Reduce-Counter,Total,1\n')
    #wordcount[current_word] = current_count
    print current_word + '\t' + str(current_count) + '\t' + str(float(current_count)/total)
    
# largest = 50
# smallest = 10
# sortedWordCount = sorted(wordcount.items(), key = operator.itemgetter(1))

# print "The Top 50 terms are"
# for i in range(largest):
#     print str(sortedWordCount[-i-1][0]) + '\t' + str(sortedWordCount[-i-1][1]) + '\t' + str(float(sortedWordCount[-i-1][1])/total)
    
# print '\n'

# print "The bottom 10 terms are"
# for i in range(smallest):
#     print str(sortedWordCount[i][0]) + '\t' + str(sortedWordCount[i][1]) + '\t' + str(float(sortedWordCount[i][1])/total)