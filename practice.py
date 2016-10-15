import hashlib
#Hash of User 0's password
user_0_hashed_pass = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
#User 0 guesses password (they have a really bad password... password)
user_0_guess = "password"
#Comparing SALT of user entered password with orignal hash
user_0_guess_hashed = hashlib.sha1(user_0_guess).hexdigest()

#if orignal hashed pass is equal to the salted guess print correct
if (user_0_hashed_pass == user_0_guess_hashed):
    print "Correct!"
