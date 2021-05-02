# PARSING HTML USING BEAUTIFULSOUP

# use 'urllib' to read the page and then use
# 'BeautifulSoup' to extract the 'href' attributes
# from the anchor 'a' tags

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")

# The list is of the links retrieved is much longer
# because some HTML anchor tags are
# relative paths (e.g., tutorial/index.html),
# in-page references(e.g., #home-page), 
# that don't include 'http://' or 'https://',
# which was a requirement in our RegEx
for tag in tags:
    print(tag.get("href", None))