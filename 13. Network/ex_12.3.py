# Use 'urllib' to replicate the previous exercise of
# (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise,
# simply show the first 3000 characters of the document contents.

# http://data.pr4e.org/romeo.txt (160ish characters, content only)
# http://data.pr4e.org/mbox.txt (6,4 millions of characters, content only)
# http://data.pr4e.org/mbox-short.txt (91.000ish characters, content only)

import urllib.request

url = input("Enter url - ")

try:
    fHand = urllib.request.urlopen(url)
except:
    print(url, "is an invalid url")
    exit()

count = 0
for line in fHand:
    line = line.decode().strip()
    # Character counts based on the length of a line
    charCount = len(line)

    # Counting the total characters
    count += charCount

    # Print the characters if it hasn't reached less than equal 3.000 characters
    if count <= 3000:
        print(line)

    # print("%s character count is %d" % (line, len(line)))
print("Total characters counted inside this document is %d" % (count))