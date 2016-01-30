#!/usr/bin/python
import sys
import re
from csv import reader

#Structure of complaints
#Complaint ID,Product,Sub-product,Issue,Sub-issue,State,ZIP code,Submitted via,Date received,Date sent to company,
#Company,Company response,Timely response?,Consumer disputed?

WORD_RE = re.compile(r"[\w']+")
for line in reader(sys.stdin):
    issue = line[3]
    if issue == '':
        issue = 'Blank'
    words = re.findall(WORD_RE, issue)
    for word in words:
        print word + '\t' + str(1)