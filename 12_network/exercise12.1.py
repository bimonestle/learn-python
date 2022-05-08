# Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL
# into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

urlAddress = input("Enter URL address: ")
try:
    splitURL = urlAddress.split('/')
    host = splitURL[2]
    mySocket.connect((host, 80))
except:
    print("Improper URL format")
    quit()

cmd = 'GET ' + urlAddress + ' HTTP/1.0\r\n\r\n'
mySocket.send(cmd.encode())

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mySocket.close()