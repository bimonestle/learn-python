import urllib.request

# Once the web page has been opened with 'urllib.urlopen',
# we can treat it like a file and read through it using a 'for' loop.
fHand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fHand:
    # When the program runs, we only see the output of the contents of the file.
    # The headers are still sent, but the 'urllib' code consumes the headers
    # and only returns the data to us.
    print(line.decode().strip())