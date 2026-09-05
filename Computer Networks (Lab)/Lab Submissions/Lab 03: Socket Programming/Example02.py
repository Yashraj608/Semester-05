import socket

host = ["www.google.com", "www.facebook.com", "www.youtube.com"]
for h in host:
    ip_address = socket.gethostbyname(h)
    print(f"IP address of {h} is {ip_address}")

