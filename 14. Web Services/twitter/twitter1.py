import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    account = input('Enter Twitter Account:')
    # If a blank line entered then quit.
    if len(account) < 1:
        break

    # Do the signing from augment() in twurl.py
    url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': '2'})
    print('Retrieving', url)
    
    connection = urllib.request.urlopen(url, context=ctx)
    # Get the unicode strings
    data = connection.read().decode()
    print(data[:250])

    # Grab the headers
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining limit:', headers['x-rate-limit-remaining'])