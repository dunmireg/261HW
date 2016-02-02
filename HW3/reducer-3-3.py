#!/usr/bin/python
import sys
import operator

total = 0
unique_items = set()
largest_basket = {}

current_item = None
current_count = None
item = None

wordcount = {}

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    
    if line[0] == '*':
        if line[1] == '0':
            total = int(line[2])
        else:
            largest_basket[line[1]] = int(line[2])
    else:
        item = line[0]
        count = int(line[1])
        unique_items.add(item)
        
        if current_item == item:
            current_count += count
        else:
            if current_item:
                wordcount[current_item] = current_count
            current_item = item
            current_count = count

if current_item == item:
    wordcount[current_item] = current_count

largest = 50
smallest = 10
#sorted_x = sorted(x.items(), key=operator.itemgetter(1))
sortedWordCount = sorted(wordcount.items(), key = lambda x: (-x[1], x[0]))

print "The Top 50 items are:"
for i in range(largest):
    print sortedWordCount[i][0] + '\t' + str(sortedWordCount[i][1]) + '\t' + str(float(sortedWordCount[i][1])/total)

print '\n'
print "The 10 smalleset items are"
for i in range(smallest):
    print sortedWordCount[-i-1][0] + '\t' + str(sortedWordCount[-i-1][1]) + '\t' + str(float(sortedWordCount[-i-1][1])/total)

print '\n'
print "Number of unique items from this supplier: " + str(len(unique_items))
print "Largest basket is " + max(largest_basket.iteritems(), key = operator.itemgetter(1))[0] + " with a basket size of " + str(max(largest_basket.iteritems(), key = operator.itemgetter(1))[1]) 

#result = max(your_dict.iteritems(), key=operator.itemgetter(1))[0]