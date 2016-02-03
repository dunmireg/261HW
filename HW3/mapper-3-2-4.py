#!/usr/bin/python
import sys
import re
from csv import reader

#Structure of complaints
#Complaint ID,Product,Sub-product,Issue,Sub-issue,State,ZIP code,Submitted via,Date received,Date sent to company,
#Company,Company response,Timely response?,Consumer disputed?

line_num = 0 #for skipping header
total = 0 #total number of words in issue
WORD_RE = re.compile(r"[\w']+")
for line in reader(sys.stdin): #here we use csv.reader to read the input of the file 
    if line_num == 0: #skip first row, which is a header
        line_num += 1
        continue
    else:
        issue = line[3] #parse the issue of the complaint
        if issue == '': #There are exactly four records where the issue was marked as blank. 
            issue = 'Blank' #We felt that setting to blank was appropriate
        words = re.findall(WORD_RE, issue)
        for word in words:
            total += 1 #increment total word counter
            print word.lower() + '\t' + str(1) #print the word and a count of 1
print '*' + '\t' + str(total) #use order inversion to provide total as first input to reducer