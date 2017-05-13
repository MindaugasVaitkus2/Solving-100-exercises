# Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

# Then just paste the following code in the file (manually):

# import requests
 
# r = requests.get("http://www.pythonhow.com")
# print(r.text[:100])
# Executing the script will throw an error. Please fix that error so that you get the expected output and explain why the error happened.

# I had to rename requests.py to requests1.py (any name would do) and I also had to delete requests.pyc. The requests.py that I created as the exercise requested was shadowing the module I really wanted to import. The error happens because python engine look for the get in the nearest requesds. that's why the solution was to rename it an to delete the pyc

#his explanation
# In the code Python is actually referring to the script name which is requests  and it doesn't find a get attribute for that name. Script names load in the current namespace. They are actually stored in the __name__  variable. You could try to print that variable out and you would see that it prints your script name. Therefore you should not name your scripts under library names. 