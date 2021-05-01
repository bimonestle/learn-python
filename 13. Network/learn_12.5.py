# READING BINARY FILES USING "urllib"

# This program reads all of the data in at once across the network
import urllib.request, urllib.parse, urllib.error

# and stores it in the variable 'img' in the main memory of your computer
img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg").read()
# then opens the file 'cover3.jpg'
# then writes the data out to your disk.
# the 'wb' argument for open(), opens a binary file for writing only.
fHand = open("cover3.jpg", "wb")
# print(img)
fHand.write(img)
fHand.close()

# This program will work if the size of the file
# is less than the size of your computer's memory.