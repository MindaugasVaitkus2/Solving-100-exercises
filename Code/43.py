# Create a script that generates a file where all letters of English alphabet are listed two in each line. The inside of the text file would look like:

# ab
# cd
# ef

# and so on.

import string
import os

if not os.path.exists('../inputs&outputs/Ex43.txt'):
    with open('../inputs&outputs/Ex43.txt', 'w') as f:
        a = (string.ascii_lowercase)
        f.write('\n'.join(l1+l2 for l1,l2 in zip(a[::2], a[1::2])))
    f.close()

# how he did
# import string

# with open("letters.txt", "w") as file:
#     for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
#         file.write(letter1 + letter2 + "\n")
