# Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL
# into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

import socket

# http://data.pr4e.org/romeo.txt
url = input("Enter url: ")

try:
    urlSplit = url.split("/")
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = urlSplit[2]
    mySock.connect((hostname, 80))
except:
    print(url, "is an invalid url")
    exit()

cmd = "GET " + url + " HTTP/1.0\r\n\r\n"
cmd = cmd.encode()
mySock.send(cmd)
while True:
    data = mySock.recv(520)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mySock.close()