#Write a script that extracts letters from the 26 text files and put the letters in a list

import glob, os
os.chdir("letters/")

letter = []
for ftext in glob.glob("*.txt"):
    print ftext
    with open(ftext, 'r') as f:
        for line in f:
            #print line
            letter.append(line.rstrip('\r\n'))
print letter

# how he did
# import glob

# letters = []
# file_list = glob.glob("letters/*.txt")
# print(file_list)
# for filename in file_list:
#     with open(filename, "r") as file:
#         letters.append(file.read().strip("\n"))

# print(letters)
