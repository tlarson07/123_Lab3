import hashlib
import random
word_list = []
start = 0
user_3 = "6108d30de651a14600a460621ea509c907c434da"

#puts the word list in an actual list
with open('words.txt','r') as f:
    for line in f:
        for words in line.split():
            word_list.append(words)

for i in range (len(word_list)):
    level_3_pass = word_list[start]
    user_3_guess_hash = hashlib.sha1(level_3_pass).hexdigest()
    if user_3_guess_hash == user_3:
        print level_3_pass
        break
    else:
        start +=1
