# Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:

# abc
# def
# ghi

# and so on.

import string
import os

if not os.path.exists('../inputs&outputs/Ex44.txt'):
    with open('../inputs&outputs/Ex44.txt', 'w') as f:
        a = string.ascii_lowercase
        f.write('\n'.join (l1+l2+l3 for l1,l2,l3 in zip(a[::3], a[1::3], a[2::3])))
    f.close()


# how he did
# import string
 
# letters = string.ascii_lowercase + " "
 
# slice1 = letters[0::3]
# slice2 = letters[1::3]
# slice3 = letters[2::3]
 
# with open("../inputs&outputs/Ex44.txt", "w") as file:
#     for s1, s2, s3 in zip(slice1, slice2, slice3):
#         file.write(s1 + s2 + s3 + "\n")

# This is like the previous exercise with the difference that we're using a different slicing step of 3 here. Another difference is that we are adding one white spaces to ascii_lowercase  so that we get a string of 27 items as opposed to 26 that ascii_lowercase  provides. By slicingascii_lowercase we would get two slices with a length of 9 and one slice with a length of 8. 

# That means the iteration would stop at the shortest slice so letters y and z wouldn't be written in the file. That's why we add a white space so we get three slices each with a length of 9. That means we get 9 iterations and not 8 as we would get with the original ascii_lowercase  string. The 9th iteration would write letters y and z in the file.

# Note that this solution might not be the best and there are surely improvements to be made so the script works with any number of letters.