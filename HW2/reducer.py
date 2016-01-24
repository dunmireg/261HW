#!/usr/bin/python
import sys

emails = set() #hold email IDs
words = {} #hold words and associated counts
spam_emails = 0 #how many emails are marked as spam
spam_word_count = 0
ham_word_count = 0

for line in sys.stdin:
    components = line.split('\t')
    
    ID = components[0]
    word = components[1]
    spam = int(components[2])
    
    if word not in words.keys():
        words[word] = {'spam_count': 0, 'ham_count': 0}
    if ID not in emails:
        emails.add(ID)
        if spam == 1:
            spam_emails += 1
        

    if spam == 1:
        words[word]['spam_count'] += 1
        spam_word_count += 1
    else:
        words[word]['ham_count'] += 1
        ham_word_count += 1


prior_spam = float(spam_emails)/len(emails)
prior_ham = 1-prior_spam

for i, word in words.iteritems():
    word['spam_like'] = float(word['spam_count'])/(spam_word_count)
    word['ham_like'] = float(word['ham_count'])/(ham_word_count)
    
print spam_word_count
print ham_word_count
# print prior_spam
# print prior_ham
# for word in words.keys():
#     print word + ', Spam: ' + str(words[word]['spam_like']) + ' Ham: ' + str(words[word]['ham_like'])