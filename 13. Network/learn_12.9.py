# USING BEAUTIFUL SOUP TO
# PULL OUT VARIOUS PARTS OF EACH TAG

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url - ")
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python3 library
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of thetag
    print("TAG:", tag)
    print("URL:", tag.get("href", None))
    print("Contents:", tag.contents[0])
    print("Attrs:", tag.attrs)