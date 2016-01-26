#!/usr/bin/python
import sys

misclassified = 0 #keep track of how many are misclassified

for line in sys.stdin:
    line = line.strip()
    line = line.rstrip()
    components = line.split('\t')
    if int(components[1]) != int(components[2]):
            misclassified += 1 #if predicted and true flag disagree increment counter
    print line
print "Misclassified: " + str(misclassified) + " which means this has an accuracy of " + str(100-misclassified) + "%"