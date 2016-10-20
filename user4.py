import hashlib
import string

user_4_hash = "0449230bb53222d50b8404f08452ffde9ac4a4d5"

def password (): #defines password as a function  
    numberOfGuesses = 0 #Initial number of guesses = 0
    for a in string.ascii_uppercase: #generates all the uppercase letters
        print a
        for b in string.ascii_uppercase: #generates all the uppercase letters
            for c in string.ascii_uppercase: #generates all the uppercase letters
                for d in string.ascii_uppercase: #generates all the uppercase letters
                    for e in string.ascii_uppercase: #generates all the uppercase letters
                        for f in string.ascii_uppercase: #generates all the uppercase letters
                            level_4_pass = a + b + c + d + e + f #sets level_4_pass as 6 random uppercases letters
                            user_4_guess_hash = hashlib.sha1(level_4_pass).hexdigest() #hash level_4_pass
                            numberOfGuesses += 1 #Increase the number of guesses by one
                            if user_4_hash == user_4_guess_hash: #if user_4_hash and user_4_guess_hash are equal prints level_4_pass and numberOfGuesses
                                print "Level 4 Password = " + level_4_pass
                                print "Attempts = " + str(numberOfGuesses)
                                return
password ()
#-----------------------------------------
#Level 4 Password = VNKHWJ
#Attempts = 255,630,658
