import hashlib
import random
#user 1 password hash
user_1 = "1b6453892473a467d07372d45eb05abc2031647a"
#
level_1_pass = str(random.randint(0,9))
user_1_guess_hash = hashlib.sha1(level_1_pass).hexdigest()

while user_1 != user_1_guess_hash:
    level_1_pass =  str(random.randint(0,9))
    user_1_guess_hash = hashlib.sha1(level_1_pass).hexdigest()
print level_1_pass

#ANSWER = 4
