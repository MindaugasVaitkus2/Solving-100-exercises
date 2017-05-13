# Please print the script in the expected output
import datetime

now = datetime.datetime.now()
#week = datetime.date.weekday()
print now.strftime('Today is %A, %B %d, %Y')
# or
print "Today is {:%A, %B %d, %Y}".format(now)