import socket

s= socket.socket()
print("Socket successfully created")

s.connect(('localhost', 9999))
print(s.recv(1024).decode())
s.close()