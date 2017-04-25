# Create a dictionary that contains the keys a  and b  and their respective values 1  and 2

key_d = ('a', 'b')
value_d = (1,2)

new_dict = dict(zip(key_d, value_d))
print new_dict
# print new_dict.keys()
# print new_dict.values()

# how he did
d = {"a": 1, "b": 2} 

# or

d = dict(a = 1, b = 2)