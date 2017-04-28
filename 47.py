#Write a script that extracts letters from files if letters are contained in "python" and puts the letters in a list

import glob, os

letter=[]

for ftext in glob.glob("letters/*.txt"):
    with open(ftext, 'r') as f:
        for line in f:
            if 'p' in line or 'y' in line or 't' in line or 'h' in line or 'o' in line or 'n' in line:
                letter.append(line.rstrip('\r\n'))
print letter

# his solution
# import glob
 
# letters = []
# file_list = glob.iglob("letters/*.txt")
# check = "python"
 
# for filename in file_list:
#     with open(filename,"r") as file:
#         letter = file.read().strip("\n")
#         if letter in check:
#             letters.append(letter)
 
# print(letters)