# Complete the script so that it removes duplicate items from list a .
from more_itertools import unique_everseen

a = ["1", 1, "1", 2]
print list(unique_everseen(a))
