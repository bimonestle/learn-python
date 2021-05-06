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

    # Create a socket
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = urlSplit[2]

    # Make a socket call to domain and port
    mySock.connect((hostname, 80))
except:
    print(url, "is an invalid url")
    exit()

# Initialize a command to a 'cmd' variable
cmd = "GET " + url + " HTTP/1.0\r\n\r\n"

# The command which was a Unicode format is converted
# to a UTF-8 format by the encode() function
cmd = cmd.encode()

# Send the command using socket
mySock.send(cmd)
while True:
    # A single character takes exactly 8 bit to stored. So that is 1B (byte).
    # So the socket ask for some certain numbers of byte
    # for the character you want to receive (hence it's called recv())
    data = mySock.recv(520)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mySock.close()