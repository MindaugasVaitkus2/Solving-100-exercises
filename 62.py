 #Create a program that once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.

import time
i = 0
while True:
    i += 1
    print ("Hello")
    time.sleep(i)
    #print i