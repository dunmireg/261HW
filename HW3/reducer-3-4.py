#!/usr/bin/python
import sys
from collections import defaultdict
import operator

support = 100
totalBaskets = 0
pairs = defaultdict(int)

for line in sys.stdin:
    line = line.split('\t')
    if line[0] == '*':
        totalBaskets = int(line[1])
    else:
        pairs[line[0]] += int(line[1])

freqDict = {}
for pair, count in pairs.iteritems():
    if count > 3:
        freqDict[pair] = count

print "Top 50 item pairs:"
print '\n'
print 'Item Pair' + '\t' + 'Support Count' + '\t' + 'Relative Support Count'
print '\n'
        
sortedFreqDict = sorted(freqDict.items(), key = lambda x: (-x[1], x[0]))
for i in range(50):
    print sortedFreqDict[i][0] + '\t' + str(sortedFreqDict[i][1]) + '\t' + str(float(sortedFreqDict[i][1])/totalBaskets)