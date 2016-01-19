#!/usr/bin/python
import sys
import re


WORD_RE = re.compile(r"[\w']+") #regex for word
filename = sys.argv[1] #get file name
findwords = re.split(" ",sys.argv[2].lower()) #parse input string of words into list
with open (filename, "r") as myfile:
    for line in myfile.readlines():
        components = line.split('\t') #split line into components ID + flag + text
        ID = components[0]
        flag = components[1]
        text = components[2] + components[3] #combine subject and content into one text list 
        word_count = {} #keep track of all words and their counts
        for word in WORD_RE.findall(text):
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        for word, count in word_count.iteritems(): 
            found_word = 0 
            if word.lower() in findwords: #check if each word is in the findword list
                found_word = 1
            #print a string with ID + spam flag + word + count + if word is a findword
            print ID + '\t' + str(flag) + '\t' + word + '\t' + str(count) + '\t' + str(found_word)