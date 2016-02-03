#!/usr/bin/python
import sys
from collections import defaultdict
import operator

support = 100 #level of support
totalBaskets = 0 #total basket
pairs = defaultdict(int) #in-memory dictionary to hold reults. This wouldn't work as a scalable solution

sys.stderr.write('reporter:counter:Reducer-Counter,Total,1\n') #increment counter
for line in sys.stdin:
    line = line.split('\t')
    if line[0] == '*': #order inversion says this will be the total 
        totalBaskets = int(line[1])
    else:
        pairs[line[0]] += int(line[1]) #increment the default dictionary for pair by counter. 
        #note when using a regular dictionary this takes an extremely long time. 

freqDict = {}
for pair, count in pairs.iteritems(): #filter dictionary for only items with support greater than level set
    if count > support: 
        freqDict[pair] = count

print "Top 50 item pairs:"
print '\n'
print 'Item Pair' + '\t' + 'Support Count' + '\t' + 'Relative Support Count'
print '\n'
        
sortedFreqDict = sorted(freqDict.items(), key = lambda x: (-x[1], x[0])) #sort results by number and by lexicographic order
for i in range(50):
    print sortedFreqDict[i][0] + '\t' + str(sortedFreqDict[i][1]) + '\t' + str(float(sortedFreqDict[i][1])/totalBaskets)