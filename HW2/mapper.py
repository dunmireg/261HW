#!/usr/bin/python

#I have placed the mapper here but have not modified it in any way from the previous mapper. It will still
#produce ID + \t + word + \t + true spam flag to send to the reducer. 
import sys
import re
import os 
from math import log
from math import exp

priorSpam = 0
priorHam = 0
words = {}

with open(os.path.join('./enroneEmailCondProbLaplace', 'part-00000'), 'r') as myfile:
    lines = myfile.readlines()
    priorSpam = float(lines[0])
    priorHam = float(lines[1])
    for line in lines[2:]:
        components = line.split('\t')
        words[components[0]] = {'spam_like': float(components[1]), 'ham_like': float(components[2])}
        

WORD_RE = re.compile(r"[\w']+")

spamSkip = 0
hamSkip = 0

for line in sys.stdin:
    components = line.split('\t')
    text = " ".join(components[-2:]).strip()
    text = re.findall(WORD_RE, text)
    
    spamScore = log(priorSpam)
    hamScore = log(priorHam)
    for word in text:
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
        pred = 0
    if spamScore > hamScore:
        pred = 1
    print components[0] + '\t' + components[1] + '\t' + str(pred) + '\t' + str(exp(spamScore)) + '\t' + str(exp(hamScore))