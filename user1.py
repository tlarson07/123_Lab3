import hashlib
import random

user_1 = "1b6453892473a467d07372d45eb05abc2031647a"
count = 0
level_1_pass = str(random.randint(0,9))
user_1_guess_hash = hashlib.sha1(level_1_pass).hexdigest()


while user_1 != user_1_guess_hash:
    level_1_pass =  str(random.randint(0,9))
    user_1_guess_hash = hashlib.sha1(level_1_pass).hexdigest()
    count += 1
print "Level 1 Password = " + level_1_pass
print "Attempts = " + str(count)
#Level 1 Password = 4
#Attempts = 28
