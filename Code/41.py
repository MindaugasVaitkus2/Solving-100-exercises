# Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

import string
import os

if not os.path.exists('../inputs&outputs/Ex41.txt'):
    with open('../inputs&outputs/Ex41.txt', 'w') as f: 

        a = list(string.ascii_lowercase)
        for letter in a:
            f.write("%s\n" % letter)
    f.close()

# how he did
# import string
 
# with open("letters.txt", "w") as file:
#     for letter in string.ascii_lowercase:
#         file.write(letter + "\n")