# Create a script that asks the user to enter their age and the script calculates the user's year of birth and print it out in a strng like in the expected output. Please make sure you generate the current year dynamicalluy

import datetime

while True:
	age = raw_input('Please enter your age: ')
	try:
		age = int(age)
		now = datetime.datetime.now()
		YearBirth =  int(now.year) - age
		print ('You were born back in %d') % YearBirth
		break
	except ValueError:
		print '%s is not a valid number. Please try again' % (age, )
