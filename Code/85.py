# Please download the attached countries_raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries.

# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or break lines in it. The new file content should look like in the expected output.

import string
import pandas as pd
import csv

fhand = open('../inputs&outputs/countries_raw.txt')
inp = fhand.read().split('\n')
#print (inp)
remove = list(string.ascii_uppercase)
remove.append('Top of Page')
f = [newf for newf in inp if newf not in remove]
#print f
FinalFile = [newf for newf in f if newf]
#print FinalFile
df = pd.DataFrame(FinalFile)
df.to_csv('../inputs&outputs/countriesEx85.txt',index=False, header=False, quoting=csv.QUOTE_NONE, escapechar='\\')


### or

with open("../inputs&outputs/countries_Ex85.txt", "w") as output:
	output.write(str(FinalFile))


# his answer
# with open("countries_raw.txt", "r") as file:
#     content = file.readlines()


# content = [i.strip("\n") for i in content if "\n" in i]

# content = [i for i in content if i !=""]
# content = [i for i in content if i !="Top of Page"]

# content = [i for i in content if len(i) != 1]
# print(content)


# with open("countries_clean.txt", "w") as file:
#     for i in content:
#         file.write(i+"\n")
