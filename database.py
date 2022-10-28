# import the library
import sqlite3 as sql
# Create db
connect = sql.connect("tiktok_user")
# create cursor
cur = connect.cursor()
# create the table
cur.execute(
    "CREATE TABLE IF NOT EXISTS tiktok(id int primary key, name text, email text)"
)
# Insert Some Data
cur.execute(
    "INSERT INTO tiktok VALUES(1, 'Mosa', 'mosa.abed@gmail.com')"
)
cur.execute(
    "INSERT INTO tiktok VALUES(2, 'ayah', 'ayah.saleem@gmail.com')"
)
cur.execute(
    "INSERT INTO tiktok VALUES(3, 'waseem', 'waseem.salman@gmail.com')"
)
cur.execute(
    "INSERT INTO tiktok VALUES(4, 'salman', 'salman.salamah@gmail.com')"
)
# SELECT Some data
data = cur.execute(
    "SELECT * FROM tiktok;"
).fetchall()

# PRint THE Data
print(*data, sep='\n')
# commit
connect.commit()
# close
connect.close()
