import socket 
host = socket.gethostname()
print(host)
ip_address = socket.gethostbyname(host)
print(ip_address)