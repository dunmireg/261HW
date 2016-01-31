#!/usr/bin/python
import sys
import re
from csv import reader

#Structure of complaints
#Complaint ID,Product,Sub-product,Issue,Sub-issue,State,ZIP code,Submitted via,Date received,Date sent to company,
#Company,Company response,Timely response?,Consumer disputed?
line_num = 0
total = 0
WORD_RE = re.compile(r"[\w']+")
for line in reader(sys.stdin):
    if line_num == 0:
        line_num += 1
        continue
    else:
        issue = line[3]
        if issue == '':
            issue = 'Blank'
        words = re.findall(WORD_RE, issue)
        for word in words:
            total += 1
            print word.lower() + '\t' + str(1)
print '*' + '\t' + str(total)