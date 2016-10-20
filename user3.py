import hashlib
import random

user_3_hash = "6108d30de651a14600a460621ea509c907c434da"
numberOfGuesses = 0 #Initial number of guesses = 0
wordListPosition = 0 #Initial position of wordList = 0
word_list = []
wordListPosition = 0
#Opens the file for words.txt For every line in the file take each word from each line and adds it to the word_list
with open('words.txt') as f:
    for line in f:
        for words in line.split():
            word_list.append(words)

#run the loop for the entire length of the word_list
for i in range (len(word_list)):
    level_3_pass = word_list[wordListPosition] #sets level_3_pass as a word
    user_3_guess_hash = hashlib.sha1(level_3_pass).hexdigest() #hash level_3_pass
    if user_3_guess_hash == user_3_hash: #if user_3_hash and user_3_guess_hash are equal prints level_3_pass and numberOfGuesses
        print "Level 3 Password = " + level_3_pass
        print "Attempts = " + str(numberOfGuesses)
        break
    else:
        wordListPosition +=1 #Increases the current position by one
        numberOfGuesses +=1 #Increase the number of guesses by one
#-----------------------------------------
#Level 3 Password = obscured
#Attempts = 65,460
