#!/usr/bin/python
import sys
import re
from math import log

emailID = set()
spam = set()
vocab = set()
spamCount = 0
spamWordCount = {}
hamCount= 0
hamWordCount = {}
foundWord = set()

files = sys.argv[1:]
for filename in files:
    with open(filename, 'r') as myfile:
        for line in myfile.readlines():
            components = line.split('\t')
            ID = components[0]
            flag = int(components[1])
            word = components[2]
            count = int(components[3])
            findword = int(components[4])
            if findword == 1:
                foundWord.add(word)
            emailID.add(ID)
            if flag == 1:
                spam.add(ID)
                spamCount += count
                if findword == 1:
                    if word not in spamWordCount:
                        spamWordCount[word] = count
                    else:
                        spamWordCount[word] += count
            else:
                hamCount += count
                if findword == 1:
                    if word not in hamWordCount:
                        hamWordCount[word] = count
                    else:
                        hamWordCount[word] += count

            
priorSpam = float(len(spam))/len(emailID)
priorHam = float(len(emailID) - len(spam))/len(emailID)


condProbSpam = {}
condProbHam = {}

for word in foundWord:
    if word in spamWordCount:
        condProbSpam[word] = float(spamWordCount[word])/spamCount
    if word in hamWordCount:
        condProbHam[word] = float(hamWordCount[word])/hamCount

        
#classify new emails
#in this case I decided to read the original file, rather than reassembling the emails from the reducer step.
#This increases modularity because in practice we would report our results on a validation or test set as opposed
#to the training set. 
WORD_RE = re.compile(r"[\w']+")    
with open('enronemail_1h.txt', 'r') as myfile:
    for line in myfile.readlines():
        components = line.split('\t')
        ID = components[0]
        trueLabel = components[1]
        text = components[2] + ' ' + components[3]
        spamScore = log(priorSpam)
        hamScore = log(priorHam)
        for word in WORD_RE.findall(text):
            if word in foundWord and word in condProbSpam:
                spamScore += log(condProbSpam[word])
            if word in foundWord and word in condProbHam:
                hamScore += log(condProbHam[word])
        predicted = 0
        if spamScore > hamScore:
            predicted = 1
        print ID + '\t' + str(trueLabel) + '\t' + str(predicted)