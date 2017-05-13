# Please concatenate this file with this one to a single text file. The content of the output file should look like below

# Expected output:
# x,y
# 3,5
# 4,9
# 6,10
# 7,11
# 8,12
# 6,10
# 8,18
# 12,20
# 14,22
# 16,24
import pandas as pd

df1 = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
df2 = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
frames = [df1, df2]
results = pd.concat(frames)
print results

results.to_csv('../inputs&outputs/results.txt', header = None, index = None, sep = ',')
