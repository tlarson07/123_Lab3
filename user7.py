import hashlib
import string

user_7 = "3e24cffc76002cfd4c3871aac82537c153531775"
word_list = []

def password ():
    count = 0
    with open('words.txt','r') as f:
        for line in f:
            for words in line.split():
                word_list.append(words)
    for a in word_list:
        if (len(a) % 10 == 0):
            print a
        for b in range (1,9):
            for c in range (10):
                for d in range (10):
                    for e in string.ascii_uppercase:
                        level_7_pass = a + str(b) + str(c) + str(d) + e
                        level_7_guess_hash = hashlib.sha1(level_7_pass).hexdigest()
                        count += 1
                        if level_7_guess_hash == user_7:
                            print "Level 7 Password = " + level_7_pass
                            print "Attempts = " + str(count)
password ()
#Level 7 Password =
#Attempts =
