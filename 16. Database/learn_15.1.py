import sqlite3
from sqlite3.dbapi2 import connect

# Makes a connection to the database stored in the file 'music.sqlite'
# in the current directory. If the file doesn't exist, it will be created.
# The reason this is called a 'connection' is that sometimes the database
# is stored on a separate 'database server' from the server on which
# we are running our application.
conn = sqlite3.connect('music.sqlite')

# A cursor is like a file handle that we can use to perform operations
# on the data stored in the database. Calling cursor() is similar conceptually
# to calling open() when dealing with text files.
# Or in a nutshell it's like a gateway to a collection of CLI
# of database commands (SQL).

# The 4 main cursors are 
# execute()
# fetchone()
# fetchall()
# close()
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)')

cur.close()