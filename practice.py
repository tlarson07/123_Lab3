import hashlib

user_0_hashed_pass = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"

user_0_guess = "password"
user_0_guess_hashed = hashlib.sha1(user_0_guess).hexdigest()

if (user_0_hashed_pass == user_0_guess_hashed):
    print "Correct!"
