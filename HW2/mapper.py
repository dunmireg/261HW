#!/usr/bin/python

#I have placed the mapper here but have not modified it in any way from the previous mapper. It will still
#produce ID + \t + word + \t + true spam flag to send to the reducer. 
import sys
import re
WORD_RE = re.compile(r"[\w']+")

for line in sys.stdin:
    components = line.split('\t')
    text = " ".join(components[-2:]).strip()
    words = re.findall(WORD_RE, text)
    for word in words:
        print components[0] + '\t' + word + '\t' + components[1]