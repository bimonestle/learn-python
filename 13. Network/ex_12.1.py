# Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL
# into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

import socket
import re

url = input("Enter url: ")
# try:
#     url = re.findall('href="(http[s]?://.*?)')
# except:
#     print("You entered an invalid url")
#     exit()
# print(url.split("/"))
urlSplit = url.split("/")
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect((urlSplit[2], 80))
cmd = "GET " + url + " HTTP/1.0\r\n\r\n"
cmd = cmd.encode()

mySock.send(cmd)

while True:
    data = mySock.recv(520)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mySock.close()