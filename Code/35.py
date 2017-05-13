# Create a function that takes any string as input and returns the number of words for that string
def count_str (string):
    count = len (string.split())
    return count

print count_str('galileo figaro magnifico')
print count_str('Esqueci o isqueiro na esquina da escola')