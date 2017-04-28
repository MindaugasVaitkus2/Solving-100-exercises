# Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

test=zip(a,b)
#print test
sumZip = [a+b for a,b in test]
print sumZip
#if it needs to be one per line:
for val in sumZip:
    print val