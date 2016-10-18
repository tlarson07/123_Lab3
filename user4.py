import hashlib
import string

user_4 = "0449230bb53222d50b8404f08452ffde9ac4a4d5"

def password ():
    count = 0
    for a in string.ascii_uppercase:
        print a
        for b in string.ascii_uppercase:
            for c in string.ascii_uppercase:
                for d in string.ascii_uppercase:
                    for e in string.ascii_uppercase:
                        for f in string.ascii_uppercase:
                            level_4_pass = a + b + c + d + e + f
                            user_4_guess_hash = hashlib.sha1(level_4_pass).hexdigest()
                            count += 1
                            if user_4 == user_4_guess_hash:
                                print "Level 4 Password = " + level_4_pass
                                print "Attempts = " + str(count)
                                return
password ()
#Level 4 Password = VNKHWJ
#Attempts = 255,630,658
