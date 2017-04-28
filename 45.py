# Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b and so on.

import string
import os

a = string.ascii_lowercase
for letter in a:
    with open(letter + ".txt", "w") as f:
        f.write(letter)
    f.close

# how he did
# import string, os

# if not os.path.exists("letters"):
#     os.makedirs("letters")
# for letter in string.ascii_lowercase:
#     with open("letters/" + letter + ".txt", "w") as file:
#         file.write(letter + "\n")
