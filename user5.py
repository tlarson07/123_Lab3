import hashlib
import string

user_5 = "8b3a437b67f90a06248180dbcfa6637cce2db8ac"

def password ():
    count = 0
    for a in string.ascii_uppercase:
        print a
        for b in string.ascii_uppercase:
            for c in string.ascii_uppercase:
                for d in range(1,9):
                    for e in range(10):
                        for f in range(10):
                            level_5_pass = a + b + c + str(d) + str(e) + str(f)
                            level_5_guess_hash = hashlib.sha1(level_5_pass).hexdigest()
                            count += 1
                            if level_5_guess_hash == user_5:
                                print "Level 5 Password = " + level_5_pass
                                print "Attempts = " + str(count)
                                return
password ()
#Level 5 Password = XGS339
#Attempts = 12,577,840
