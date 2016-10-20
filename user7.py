import hashlib
import string

#Hash of user 7 password
user_7 = "3e24cffc76002cfd4c3871aac82537c153531775"
#Puts the word list in an ACTUAL List
word_list = []

def password ():
    numberOfGuesses = 0 #Initial number of guesses = 0
    with open('words.txt') as f:
        for line in f:
            for words in line.split():
                word_list.append(words)
    for b in range (1,9): #(9 possiblities)
        for c in range (10): #(10 possiblities)
            for d in range (10): #(10 possiblities)
                for e in string.ascii_uppercase: #(26 possiblities)
                    for a in word_list: #notice how word_list is last (99,171 possiblities)
                        level_7_pass = a + str(b) + str(c) + str(d) + e
                        level_7_guess_hash = hashlib.sha1(level_7_pass).hexdigest()
                        numberOfGuesses += 1
                        if level_7_guess_hash == user_7:
                            print "Level 7 Password = " + level_7_pass
                            print "Attempts = " + str(numberOfGuesses)
                            return
password ()
#-----------------------------------------
#Level 7 Password = strangest121S
#Attempts = 56,019,399
