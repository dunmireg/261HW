#!/usr/bin/python
import sys
from itertools import combinations

totalBaskets = 0 #field to hold total number of baskets
sys.stderr.write('reporter:counter:Mapper-Counter,Total,1\n') #increment mapper counter
for line in sys.stdin:
    totalBaskets += 1 #increment
    line = line.strip()
    line = line.split()
    
    pairs = list(combinations(line, 2)) #this give all pair combinations for all items in a basket
    for pair in pairs:
        pair = sorted(list(pair)) #sort the pairs in lexicographic order
        print pair[0] + ' ' + pair[1] + '\t' + str(1) #print result: item1 + item2 + count of 1
print '*' + '\t' + str(totalBaskets) #print total baskets