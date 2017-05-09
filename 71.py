# Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

import requests
from collections import Counter

t = requests.get("http://www.pythonhow.com/data/universe.txt")
words = t.text
print words
words_count = Counter(words.split())
#print words_count
#print sum(words_count.values())
sub='a'
print words.count(sub)