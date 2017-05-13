#Please download the database file database.db and use Python to access the database table rows that have an area of 2,000,000 or greater. Then export those rows to a CSV file
import sqlite3
import pandas as pd

con = sqlite3.connect('../inputs&outputs/database.db')
table = pd.read_sql_query('SELECT * from countries WHERE area > 2000000', con)
table.to_csv('../inputs&outputs/database_Ex90.csv', index = False)

# how he did
# import sqlite3
# import pandas
#
# conn = sqlite3.connect("database.db")
# cur = conn.cursor()
# cur.execute("SELECT * FROM countries WHERE area >= 2000000")
# rows = cur.fetchall()
# conn.close()
#
# print(rows)
#
# df = pandas.DataFrame.from_records(rows)
# df.columns =["Rank", "Country", "Area", "Population"]
# print(df)
# df.to_csv("countries_big_area.csv", index=False)
