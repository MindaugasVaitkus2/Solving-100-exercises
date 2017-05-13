# Filter the dictionary by removing all items with a value of greater than 1
d = {"a": 1, "b": 2, "c": 3}

new_d = {k:v for k,v in d.items() if v <= 1 }
print new_d