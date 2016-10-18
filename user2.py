import hashlib
import random

user_2 = "5c1dc07026ceafcb704bdff1375815f30a769a13"
level_2_pass = str(random.randint(1,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
user_2_guess_hash = hashlib.sha1(level_2_pass).hexdigest()

while user_2 != user_2_guess_hash:
    level_2_pass = str(random.randint(1,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    user_2_guess_hash = user_2_guess_hash = hashlib.sha1(level_2_pass).hexdigest()
print level_2_pass

int = 0
for a in range(10):
    int += 1

#ANSWER = 747
