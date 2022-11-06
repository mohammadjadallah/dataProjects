import sqlite3
import pandas as pd

con = None
try:
    con = sqlite3.connect('s.sql')
    print("DataBase connected")
except Exception as e:
    print(e)

# make some queries using pandas
cur = con.cursor()
# create table
cur.execute("create table if not exists yazan_table(id integer, name text, age integer)")
cur.execute("insert into yazan_table values(1, 'mosa', 18)")
cur.execute("insert into yazan_table values(2, 'salman', 22)")
cur.execute("insert into yazan_table values(3, 'haleem', 42)")
cur.execute("insert into yazan_table values(4, 'waleed', 56)")
cur.execute("insert into yazan_table values(5, 'sameer', 80)")
con.commit()

print(pd.read_sql_query('SELECT * FROM yazan_table', con))
