# Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries
import pandas as pd

df = pd.read_csv('../inputs&outputs/countries-by-area.txt')
df ['density_pop'] = df['population_2013'] / df['area_sqkm']
#print (df.head())
result = df.sort_values(by='density_pop', ascending = 0)
print (result['country'].head())
# or
for i in result['country'][:5].tolist():
	print i
 #or
print result['country'][:5]


# how he did
# import pandas
#
# data = pandas.read_csv("countries_by_area.txt")
# data["density"] = data["population_2013"] / data["area_sqkm"]
# data = data.sort_values(by="density", ascending=False)
#
# for index, row in data[:5].iterrows():
#     print(row["country"])
