#!/usr/bin/python
import sys

misclassified = 0

for line in sys.stdin:
    components = line.split('\t')
    if len(components) != 1:
        if int(components[1]) != int(components[2]):
                misclassified += 1
        print line
    else:
        print line
print "Misclassified: " + str(misclassified) + " which means this has an accuracy of " + str(100-misclassified) + "%"
    