# (Advanced)
# Change the socket program so that it only shows data
# after the headers and a blank line have been received.
# Remember that recv receives characters (newlines and all), not lines.

import socket

# http://data.pr4e.org/romeo.txt (500ish characters, include file header)
# http://data.pr4e.org/mbox.txt (Millions of characters, include file header)
# http://data.pr4e.org/mbox-short.txt (95.000ish characters, include file header)

url = input("Enter Url - ")

try:
    urlSplit = url.split("/")

    # Create socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    domain = urlSplit[2]

    # Make a socket call to domain and port
    mysock.connect((domain, 80))

except:
    print("%s is an invalid url" % (url))
    exit()

# Initialize a command to cmd variable
cmd = "GET " + url + " HTTP/1.0\r\n\r\n"

# The command which was a "Unicode"
# is converted to UTF-8 by the 'encode()' function
cmd = cmd.encode()

# Send the command using socket
mysock.send(cmd)

resp = list()
while True:
    # A single character takes exactly 8 bit to stored. So that is 1 B (byte).
    # So the socket ask and receive (hence why it's called 'recv()') every single character.
    # 1 byte == 1 character.
    data = mysock.recv(520)
    if len(data) < 1:
        break
    
    resp.append(data.decode())

mysock.close()

print(resp)
# Join all elements without a separator
resp = "".join(resp)

# Split respons based on 'return' and 'newline' character.
# Choose the body document from the second element
body = resp.split("\r\n\r\n")[1]
# print(body)