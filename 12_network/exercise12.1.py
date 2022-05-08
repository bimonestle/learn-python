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