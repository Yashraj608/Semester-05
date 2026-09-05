import time 
import socket

start_time = time.time()

target = input("Enter the host to be scanned: ")
print("Starting port scanning on host:", target)
try:
 for port in range(50,100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target,port))

    if result ==0:
        print("Port {} is open".format(port))

    s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting program.")
    exit()
except socket.error:
    print("Couldn't connect to server. Exiting program.")
    exit()

print("port scanning completed in {:.2f} seconds".format(time.time() - start_time))