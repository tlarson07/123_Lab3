import hashlib
import random

user_2 = "5c1dc07026ceafcb704bdff1375815f30a769a13"
count = 0

int = 0
for a in range(1,9):
    for b in range(10):
        for c in range(10):
            level_2_pass = str(a) + str(b) + str(c)
            user_2_guess_hash = hashlib.sha1(str(level_2_pass)).hexdigest()
            count += 1
            if user_2 == user_2_guess_hash:
                print "Level 2 Password = " + level_2_pass
                print "Attempts = " + str(count)
#Level 2 Password = 747
#Attempts = 648
