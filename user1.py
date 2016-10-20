import hashlib
import random


user_1_hash = "1b6453892473a467d07372d45eb05abc2031647a"
numberOfGuesses = 0 #Initial number of guesses = 0
level_1_pass = str(random.randint(0,9)) #sets level_1_pass as a variable
user_1_guess_hash = hashlib.sha1(level_1_pass).hexdigest() #sets user_1_guess_hash as a variable

#continue running the loop while the user_1_hash is different from the user_1_guess_hash
while user_1_hash != user_1_guess_hash:
    level_1_pass =  str(random.randint(0,9)) #randomly generate an int between 0 and 9
    user_1_guess_hash = hashlib.sha1(level_1_pass).hexdigest() #hash the password generated from above
    numberOfGuesses += 1 #Increase the number of guesses by one
print "Level 1 Password = " + level_1_pass #print password
print "Attempts = " + str(numberOfGuesses) #print number of guesses
#-----------------------------------------
#Level 1 Password = 4
#Attempts = 4
