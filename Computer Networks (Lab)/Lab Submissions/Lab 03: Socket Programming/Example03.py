import socket

try:
    result = socket.gethostbyaddr("8.8.8.8")
    print("Hostname:", result)
except socket.herror:
    print("Could not resolve hostname.")