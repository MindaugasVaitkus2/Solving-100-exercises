#When writing web apps, you may need to generate default random passwords for users.
#Create a program that generates a password of 6 random alphanumeric characters in the range abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?

import string
from random import *

characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(6,6)))
print password

# his answer
# import random
 
# characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# chosen = random.sample(characters, 6)
# password = "".join(chosen)
# print(password)