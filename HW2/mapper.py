#!/usr/bin/python

#I have placed the mapper here but have not modified it in any way from the previous mapper. It will still
#produce ID + \t + word + \t + true spam flag to send to the reducer. 
import sys
import re
import os 
from math import log
from math import exp

priorSpam = 0 #priors
priorHam = 0
words = {}

with open(os.path.join('./enroneEmailCondProbLaplace', 'part-00000'), 'r') as myfile: #read input file
    lines = myfile.readlines() #parse lines
    priorSpam = float(lines[0]) #get priors
    priorHam = float(lines[1])
    for line in lines[2:]:
        line = line.strip()
        line = line.rstrip()
        components = line.split('\t') #split remaining lines and add word and likelihoods to dictionary
        words[components[0]] = {'spam_like': float(components[1]), 'ham_like': float(components[2])}
        

WORD_RE = re.compile(r"[\w']+")

for line in sys.stdin: #read input
    line = line.strip()
    line = line.rstrip()
    components = line.split('\t')
    text = " ".join(components[-2:]).strip() #get subject and content together as text
    text = re.findall(WORD_RE, text)
    
    spamScore = log(priorSpam) #get priors
    hamScore = log(priorHam)
    for word in text:
        if word in words.keys(): #increment scores based on word conditional probabilities
            spamScore += log(float(words[word]['spam_like']))
            hamScore += log(float(words[word]['ham_like']))
        pred = 0 #predicted class
    if spamScore > hamScore:
        pred = 1
    #output ID, spam flag, predicted class, and exponentiated conditional probabilities for document
    print components[0] + '\t' + components[1] + '\t' + str(pred) + '\t' + str(exp(spamScore)) + '\t' + str(exp(hamScore))