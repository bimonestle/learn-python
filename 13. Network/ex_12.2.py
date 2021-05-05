# Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters
# and display the count of the number of characters at the end of the document.

import socket

# http://data.pr4e.org/romeo.txt (500ish characters, include file header)
# http://data.pr4e.org/mbox.txt (Millions of characters, include file header)
# http://data.pr4e.org/mbox-short.txt (95.000ish characters, include file header)
url = input("Enter - ")

try:
    urlSplit = url.split("/")
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = urlSplit[2]
    mysock.connect((hostname, 80))
except:
    print(url, "is an invalid url")
    exit()

cmd = "GET " + url + " HTTP/1.0\r\n\r\n"
cmd = cmd.encode()
mysock.send(cmd)
count = 0
while True:
    data = mysock.recv(1)
    count += 1
    if len(data) < 1:
        break
    if count <= 3000:
        print(data.decode(), end="")

print("\n%d characters count" % (count))
mysock.close()