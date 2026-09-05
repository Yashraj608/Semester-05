import socket
import json 

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost', 9999))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

data = {
    "num1": num1,
    "num2": num2,
    "operation": operation
}

message = json.dumps(data)
s.send(message.encode())

result = s.recv(1024).decode()
print("Result:", result)