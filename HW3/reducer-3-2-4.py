#!/usr/bin/python
import sys
import operator

current_word = None #follows same basic structure as word count we have worked with before
current_count = None
word = None
total = 0
#wordcount = {} #a dictionary to store counts. This was used in an earlier version using an in-memory mapper

for line in sys.stdin:
    line = line.split('\t') #split line
    word = line[0] #read word
    count = int(line[1]) #get count
    if word == '*':
        total = count #if the word is * we know this is the total number of words and set this as a field
    else: #otherwise continue as normal
        if current_word == word: 
            current_count += count
        else:
            if current_word:
                #wordcount[current_word] = current_count #used in in-memory dictionary version
                #structure of result is word + count + relative count
                print current_word + '\t' + str(current_count) + '\t' + str(float(current_count)/total) #print result
            current_word = word
            current_count = count

#print last word
if current_word == word:
    #wordcount[current_word] = current_count
    print current_word + '\t' + str(current_count) + '\t' + str(float(current_count)/total)
    
#Code for in-memory dictionary printing
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