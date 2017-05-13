#  Complete the script so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
# Expected output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'] 
my_range = range(1, 21)
str_list = [str(x) for x in my_range]
print str_list
# or
print [str(x) for x in my_range]

# how he did
print(list(map(str, my_range)))

# map applies a function to an iterable object