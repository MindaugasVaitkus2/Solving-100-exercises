#Create a program that prints out Hello  every two seconds.

import time
starttime=time.time()
while True:
    print "Hello"
    time.sleep(2.0 - ((time.time() - starttime) % 2.0))

# his answer
# import time
 
# while True:
#     print("Hello")
#     time.sleep(2)
