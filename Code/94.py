#  Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:
# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com
# Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.
fhand = open('../inputs&outputs/urls.txt')
inp = fhand.read().split()
new = [item.replace('https:/', 'http://') for item in inp]
#print new

with open('../inputs&outputs/urls_Ex94.txt', 'w') as file:
    for i in new:
        file.write(i+'\n')

# how he did
# with open("urls.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

# with open("urls_corrected.txt", "w") as file:
#     for line in lines:
#         line_remove_s = line.replace("s", "", 1)
#         print(line_remove_s)
#         line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[6:]
#         print(line_remove_s_add_slash)
#         file.write(line_remove_s_add_slash)
