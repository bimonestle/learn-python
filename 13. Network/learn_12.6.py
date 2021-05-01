# In order to avoid running out of memory,
# we retrieve the data in blocks (or buffers) and then
# write each block to your disk before retrieving the next block.
# This way, the program can read any size file without using up
# all of the memory you have in your computer.

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
fHand = open("cover3.jpg", "wb")
size = 0
while True:
    # We read only 100.000 characters at a time
    info = img.read(100000)
    if len(info) < 1:
        break
    size += len(info)
    # write the characters onto the 'cover.jpg' file
    # before retrieving the next 100.000 characters of data from the web.
    fHand.write(info)

print(size, "characters copied.")
fHand.close()