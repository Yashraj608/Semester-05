import socket 
def service_name():
    port = [80,22,20,25]
    for p in port:
        service = socket.getservbyport(p)
        print(f"Service name for port {p} is {service}")

if __name__ == "__main__":
    service_name()