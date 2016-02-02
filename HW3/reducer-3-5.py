#!/usr/bin/python
import sys
import ast
from collections import Counter, OrderedDict

support = 3
totalBaskets = 0
current_item = None
current_item_dict = Counter({})

for line in sys.stdin:
    line = line.strip().split('\t')
    
    if line[0] == '*':
        totalBaskets = int(line[1])
    else:
        item = line[0]
        item_dict = line[1]
        item_dict = Counter(eval(item_dict))
        if current_item == item:
            current_item_dict += Counter(item_dict)
        else:
            if current_item:
                for i in OrderedDict(sorted(current_item_dict.items())):
                    if current_item_dict[i] >= support:
                        print current_item + ' ' + i + '\t' + str(current_item_dict[i]) + '\t' + str(float(current_item_dict[i])/totalBaskets)
            current_item = item
            current_item_dict = item_dict
            
for i in OrderedDict(sorted(current_item_dict.items())):
    if current_item_dict[i] >= support:
        print current_item + ' ' + i + '\t' + str(current_item_dict[i]) + '\t' + str(float(current_item_dict[i])/totalBaskets)