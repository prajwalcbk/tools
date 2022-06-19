#!/usr/bin/python3


import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=444

serversocket.bind(("192.168.43.24",port))

serversocket.listen(3)
try:
    while True:
        clientsocket,address=serversocket.accept()
        print("Connection established from "+str(address))
        message="Hello!, Thank you for connecting to the server"
        clientsocket.send(message.encode('ascii'))
        clientsocket.close()
except KeyboardInterrupt:
    print("\n KEY INTERRUPTED")