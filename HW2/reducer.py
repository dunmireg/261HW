#!/usr/bin/python
import sys
import os
from math import log
from math import exp

priorSpam = 0
priorHam = 0
words = {}

with open(os.path.join('./enroneEmailCondProbs', 'part-00000'), 'r') as myfile:
    lines = myfile.readlines()
    priorSpam = float(lines[0])
    priorHam = float(lines[1])
    for line in lines[2:]:
        components = line.split('\t')
        words[components[0]] = {'spam_like': float(components[1]), 'ham_like': float(components[2])}

        
curID = None
spamSkip = 0
hamSkip = 0
spamScore = log(priorSpam)
hamScore = log(priorHam)
curflag = 0

for line in sys.stdin:
    components = line.split('\t')
    ID = components[0]
    word = components[1]
    flag = int(components[2])
    
    if curID == ID:
        if word in words.keys():
            if float(words[word]['spam_like']) != 0:
                spamScore += log(float(words[word]['spam_like']))
            else:
                spamScore += -300
                spamSkip += 1
            if float(words[word]['ham_like']) != 0:
                hamScore += log(float(words[word]['ham_like']))
            else:
                hamScore += -300
                hamSkip += 1
#             if float(words[word]['spam_like']) != 0.0 and float(words[word]['ham_like']) != 0.0:
#                 spamScore += log(float(words[word]['spam_like']))
#                 hamScore += log(float(words[word]['ham_like']))
    else:
        if curID:
            classification = 0
            if spamScore > hamScore:
                classification = 1
            print curID + '\t' + str(flag) + '\t' + str(classification) + '\t' + str(exp(spamScore)) + '\t' + str(exp(hamScore))
        curID = ID
        curflag = flag
        spamScore = log(priorSpam)
        hamScore = log(priorHam)
    
if ID == curID:
    print curID + '\t' + str(flag) + '\t' + str(classification) + '\t' + str(exp(spamScore)) + '\t' + str(exp(hamScore))
    print spamSkip
    print hamSkip