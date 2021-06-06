# One of the problems of any kind of spidering program is that it needs to be able
# to be stopped and restarted many times and you don't want to lose the data that
# you have retrieved so far. You don't want to always restart your data retrieval
# at the very beginning so we want to store data as we retrieve it so our program
# can start back up and pick up where it left off.

# We will start by retrieving one person's Twitter friends and their statuses,
# looping through the list of friends, and adding each of the friends
# to a database to be retrieved in the future.

# After we process one person's Twitter friends, we check in our database
# and retrieve one of the the friends of the friend. We do this over and over,
# picking an 'unvisited' person, retrieving their friend list,
# and adding friends we have not seen to our list for a future visit.

# We also track how many times we have seen a particular friend in the database
# to get some sense of their popularity.

# By storing our list of known accounts and whether we have retrieved the account
# or not, and how popular the account is in a database on the disk of the computer,
# we can stop and restart our program as many times as we like.

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)
''')

# Ignore SSL certificate 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    account = input('Enter a Twitter account or quit: ')
    if account == 'quit':
        break
    if len(account) < 1:
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            account = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': '20'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # json.dumps(js, indent=4) # print

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (account, ))

    countNew = 0
    countOld = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))

        try:
            count = cur.fetchone()[0]
            cur.execute('SELECT friends FROM Twitter WHERE name = ?', (count+1, friend))
            countOld += 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)''', (friend, ))
            countNew += 1
    print('New Accounts = %d, Revisited = %d' % (countNew, countOld))
    conn.commit()

cur.close()