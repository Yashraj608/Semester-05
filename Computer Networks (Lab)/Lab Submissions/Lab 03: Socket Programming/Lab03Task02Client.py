import socket

s= socket.socket()
print("Socket successfully created")

Points = float(input("Enter your points: "))
s.connect(('localhost',9999))
data = {
    "Points": Points}
s.send(str(Points).encode())

response = s.recv(1024).decode()
print("Response from server:", response)
s.close()