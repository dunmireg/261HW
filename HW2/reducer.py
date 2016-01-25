#!/usr/bin/python
import sys

misclassified = 0

for line in sys.stdin:
    components = line.split('\t')
    if int(components[1]) != int(components[2]):
            misclassified += 1
    print line
print "Misclassified: " + str(misclassified) + " which means this has an accuracy of " + str(100-misclassified) + "%"