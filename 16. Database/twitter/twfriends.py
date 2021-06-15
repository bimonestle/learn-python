# This program is starting a bit complicated, but it illustrates the patterns
# that we need to use when we are using integer keys to link tables.
# The basic patterns are:
# 1. Create tables with primary keys and constraints.
# 2. When we have a logical key for a person (i.e., account name) and we need
# the 'id' value for the person, depending on whether or not the person is already
# in the 'People' table we either need to:
#   a. Look up the person in the 'People' table and
#   retrieve the 'id' value for the person or
#   b. add the person to the 'People' table and get
#   the 'id' value for the newly added row.
#   c. Insert the row that captures the 'follows' relationship.


from sqlite3.dbapi2 import connect
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

# We indicate the 'name' column in the 'People' table must be 'UNIQUE'.
cur.execute('''CREATE TABLE IF NOT EXISTS People (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')

# We also indicate that the combination of the two numbers in each row
# of the 'Follows' table must be unique. These constraints keep us from
# making the same mistakes such as adding the same relationship
# more than once.
cur.execute('''CREATE TABLE IF NOT EXISTS Follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # When we prompt the user for a Twitter account, if the account exists,
    # we must look up its 'id' value. If the account doesn't yet exist
    # in the database ('People' table), we must insert the record and get the
    # 'id' value from the inserted row
    account = input('Enter a Twitter Account or quit: ')
    if account == 'quit':
        break
    if len(account) < 1:
        cur.execute('SELECT id, name FROM People where retrieved = 0 LIMIT = 1')
        try:
            (id, account) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT = 1', (account,))
        try:
            id = cur.fetchone()[0]
        except:
            # We add the 'OR IGNORE' clause into our 'INSERT' statement to indicate that
            # if this particular 'INSERT' would cause a violation of the 'name must be unique' rule,
            # the database system is allowed to ignore the 'INSERT'.
            # We are using the database constraint as a safety net to make sure
            # we don't inadvertently do something incorrect.
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)''', (account,))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', account)
                continue
            id = cur.lastrowid
    
    url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': 100})
    print('Retrieving account', account)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (account,))

    countNew = 0
    countOld = 0

    # This is a very common pattern and is done twice in the program above.
    # This code shows how we look up the 'id' for a friend's account
    # when we have extracted 'screen_name' from a 'user' node
    # in the retrieved Twitter JSON.

    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        # Since overtime it will be increasingly likely that the account will aready be
        # in the database, we first check to see if the 'People' record exists using
        # a 'SELECT' statement.
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend,))

        # If all goes well inside the 'try' section, we retrieve the record using
        # 'fetchone()' and then retrieve the first (and only) element of the
        # returned tuple and store it 'friend_id'.
        try:
            friend_id = cur.fetchone()[0]
            countOld += 1
        
        # If the 'SELECT' fails, the 'fetchone()[0]' code will fail and
        # control will transfer into 'except' section.
        
        # If we end up in the 'except' code, it simply means that the row
        # was not found, so we must insert the row.
        # We use 'INSERT OR IGNORE' just to avoid errors and then call 'commit()'
        # to force the database to really be updated.
        # After the write is done, we can check the 'cur.rowcount' to see
        # how many rows were afected. Since we are attempting to insert a single row,
        # if the number of affected rows is something other than 1, it's an error.

        # If the 'INSERT' is successful, we can look at cur.lastrowid to find out
        # what value the database assigned to the 'id' column in our newly created row.
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)''', (friend,))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countNew += 1
        
        # We simply tell the database to ignore our attempted 'INSERT',
        # if it would violate the uniqueness constraint that we specified for the 'Follows' rows.
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)''', (id, friend_id))
        print('New Accounts=', countNew, 'revisited=', countOld)
        print('Remaining', headers['x-rate-limit-remaining'])
        conn.commit()
    cur.close()
