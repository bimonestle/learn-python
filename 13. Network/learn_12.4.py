# RETRIEVE THE DATA FROM THE WEB
# AND READ IT LIKE A LOCAL FILE

import urllib.request, urllib.parse, urllib.error

fHand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fHand:
    line = line.decode().rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)