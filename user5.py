import hashlib
import string

user_5 = "8b3a437b67f90a06248180dbcfa6637cce2db8ac"

def password (): #defines password as a function  
    numberOfGuesses = 0 #Initial number of guesses = 0
    for a in string.ascii_uppercase: #generates all the uppercase letters
        print a
        for b in string.ascii_uppercase: #generates all the uppercase letters
            for c in string.ascii_uppercase: #generates all the uppercase letters
                for d in range(1,9): #generates all the ints between 1 and 9
                    for e in range(10): #generates all the ints between 0 and 10
                        for f in range(10): #generates all the ints between 0 and 10
                            level_5_pass = a + b + c + str(d) + str(e) + str(f) #sets level_5_pass as 3 uppercase letters and 3 ints
                            level_5_guess_hash = hashlib.sha1(level_5_pass).hexdigest() #hash level_5_pass
                            numberOfGuesses += 1 #Increase the number of guesses by one
                            if level_5_guess_hash == user_5: #if user_5_hash and user_5_guess_hash are equal prints level_5_pass and numberOfGuesses
                                print "Level 5 Password = " + level_5_pass
                                print "Attempts = " + str(numberOfGuesses)
                                return
password ()
#-----------------------------------------
#Level 5 Password = XGS339
#Attempts = 12,577,840
