# Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters
# and display the count of the number of characters at the end of the document.

# http://data.pr4e.org/romeo.txt

import socket
import time

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

count = 0
while True:
    data = mySocket.recv(500)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count += len(data)
    print(data.decode(), end='')
    print("\nTotal length data: %d. Counting: %d" % (len(data), count))
    if count == 3000:
        break

print("Total length data: %d. Counting: %d" % (len(data), count))
mySocket.close()