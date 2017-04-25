# Complete the script so that it removes duplicate items from list a .
from more_itertools import unique_everseen

a = ["1", 1, "1", 2]
a = list(unique_everseen(a))
print a

# how he did
a = list(set(a))
print(a)

# or

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# or

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)