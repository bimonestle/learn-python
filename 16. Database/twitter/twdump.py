# This program simply opens the database and selects all of the columns
# of all of the rows in the table Twitter, then loops through the rows and prints out each row.

import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Twitter')
count = 0
for row in cur:
    print(row)
    count += 1
print(count, 'rows.')
cur.close()