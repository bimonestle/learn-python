import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# Drop the Table if it already exists, Otherwise create the table
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(Title TEXT, Plays INTEGER)')

# Insert Data to the table
cur.execute('INSERT INTO Tracks (Title, Plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (Title, Plays) VALUES (?, ?)', ('My Way', 15))
# Use commit to force the data to be written to the database file
conn.commit()

print('Tracks:')
# Select the Title & Plays column from Tracks table
cur.execute('SELECT Title, Plays FROM Tracks')
for row in cur:
    # each row is a Python tuple (title, plays)
    print(row)

# We execute an SQL command to DELETE the rows we have just created so we can run the program over and over.
# cur.execute('DELETE FROM Tracks WHERE Plays < 100')
conn.commit()

cur.close()