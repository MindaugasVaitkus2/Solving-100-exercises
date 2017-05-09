# Print out the text of this file http://www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.

import requests

t = requests.get('http://www.pythonhow.com/data/universe.txt')
print (t.text)