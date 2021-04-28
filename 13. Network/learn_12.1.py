# Learn How The Protocol Works

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The program makes a connection to port 80 on the server www.py4e.com
# Our program is playing the role of the "web browser".
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()

# The HTTP protocol says we must send the 'GET' command followed by a blank line
# '\r\n' signifies EOL (End of Line).
# '\r\n\r\n' signifies nothing between two EOL sequences. That is the equivalent of a blank line.
mysock.send(cmd)

# Once we send the blank line, we write a loop that receives data in 512-character chunks
# from the socket and prints out the data out until there's no more to read.
# i.e., the recv() returns an empty string.
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mysock.close()