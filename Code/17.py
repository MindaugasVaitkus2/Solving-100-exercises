# Calculate the sum of the values of keys a  and b
d = {"a": 1, "b": 2, "c": 3}
#print d.items()
new_dict = {k: v for k,v in d.items() if k != "c"}
list_val = new_dict.values()
print sum (list_val)

# or

print sum(new_dict.values())

# how he did
print(d["b"] + d["a"])