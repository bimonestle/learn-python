# Change the urllinks.py program to extract and count paragraph (p) tags
# from the retrieved HTML document and display the count of the paragraphs
# as the output of your program. Do not display the paragraph text, only count them.
# Test your program on several small web pages as well as some larger web pages.

# http://data.pr4e.org/romeo.txt (160ish characters, content only)
# http://data.pr4e.org/mbox.txt (6,4 millions of characters, content only)
# http://data.pr4e.org/mbox-short.txt (91.000ish characters, content only)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the <p> or paragraph tags
tags = soup("p")
count = 0
for tag in tags:
    count += 1
    print(tag)
print("p tag is counted %d times" % (count))