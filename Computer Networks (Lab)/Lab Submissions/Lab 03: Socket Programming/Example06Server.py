import socket

s= socket.socket()
print("Socket successfully created")

s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connections")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send(b'Thank you for connecting')
    c.close()