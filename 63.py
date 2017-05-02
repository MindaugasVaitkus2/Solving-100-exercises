# Create a program that once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

import time

i = 0
while True:
    i += 1
    print ('Hello')
    time.sleep(i)
    if i > 3:
        break
print 'End of Loop'

#his answer
# i = 0
# while True:
#     print("Hello")
#     i = i + 1
#     if i > 3:
#         print("End of loop")
#         break
#     time.sleep(i)
