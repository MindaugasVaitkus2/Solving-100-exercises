# Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out
import pprint

k = ['a', 'b', 'c']
v = [range(1,11), range(11,21), range(21,31)]
#pprint.pprint (v)
new_dict = dict(zip(k,v))
pprint.pprint (new_dict)

# how he did
from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d)