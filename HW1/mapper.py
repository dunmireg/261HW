#!/usr/bin/python
import sys
import re


WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[1]
findwords = re.split(" ",sys.argv[2].lower())
with open (filename, "r") as myfile:
    for line in myfile.readlines():
        components = line.split('\t')
        ID = components[0]
        flag = components[1]
        text = components[2] + components[3]
        word_count = {}
        for word in WORD_RE.findall(text):
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        for word, count in word_count.iteritems():
            found_word = 0
            if word.lower() in findwords:
                found_word = 1
            print ID + '\t' + str(flag) + '\t' + word + '\t' + str(count) + '\t' + str(found_word)