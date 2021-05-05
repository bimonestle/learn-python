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

    # Create a socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    domain = urlSplit[2]

    # Make a socket call to a domain and port
    mysock.connect((domain, 80))
except:
    print(url, "is an invalid url")
    exit()

# Initialize a command to cmd variable
cmd = "GET " + url + " HTTP/1.0\r\n\r\n"

# The command which was a 'Unicode' is converted to
# UTF-8 by the 'encode()' function
cmd = cmd.encode()

# Send the command using socket
mysock.send(cmd)
count = 0
while True:
    # A single character takes exactly 8 bit to be stored. So that is 1B (byte).
    # So the socket ask and receive (hence why it's called 'recv()') every single character (1 byte == 1 character)
    data = mysock.recv(1)
    count += 1
    if len(data) < 1:
        break

    # If the character count reaches up to 3.000 characters,
    # convert it back to Unicode and print it
    if count <= 3000:
        print(data.decode(), end="")

print("\n%d characters count" % (count))
mysock.close()