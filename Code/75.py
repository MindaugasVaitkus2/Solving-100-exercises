#Plot the data in the file provided through the URL http://www.pythonhow.com/data/sampledata.txt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
plt.figure()
#this:
#df.plot(x = 'x', y = 'y', style = 'o')
# or
plt.scatter(df['x'], df['y'])
plt.title('Exercise 75')
plt.ylabel('y')
plt.xlabel('x')
plt.axis([0,int(max(df['x'])) + 1, 0, int(max(df['y'])) + 2] )
plt.grid(True)
plt.savefig('../inputs&outputs/Figure75.png')
plt.show()
