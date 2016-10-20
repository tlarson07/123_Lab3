import hashlib
import random

user_2_hash = "5c1dc07026ceafcb704bdff1375815f30a769a13"
numberOfGuesses = 0 #Initial number of guesses = 0

for a in range(1,9): #generates all the ints between 1 and 9
    for b in range(10): #generates all the ints between 0 and 10
        for c in range(10): #generates all ints between 0 and 10
            level_2_pass = str(a) + str(b) + str(c) #sets level_2_pass as 
            user_2_guess_hash = hashlib.sha1(str(level_2_pass)).hexdigest() #hashing the password
            numberOfGuesses += 1 #Increase the number of guesses by one
            if user_2_hash == user_2_guess_hash: #if user_2_hash and user_2_guess_hash are equal prints passwords and number guesses
                print "Level 2 Password = " + level_2_pass
                print "Attempts = " + str(numberOfGuesses)
#-----------------------------------------
#Level 2 Password = 747
#Attempts = 648
