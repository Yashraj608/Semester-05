import socket
import json
s= socket.socket()
s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connections")

c,address = s.accept()
print("Got connection from", address)
data = c.recv(1024).decode()

message = json.loads(data)

num1 = message["num1"]
num2 = message["num2"]
operation = message["operation"]

if operation == "+":
    result = num1+num2

elif operation == "-":
    result = num1-num2  
elif operation == "*":
    result = num1*num2
elif operation == "/":
    if num2 ==0:
        result = "Error: Division by zero"
    else:
        result = num1/num2
else:
    result = "Error: Invalid operation"


details = {
    "num1": num1,
    "num2": num2,
    "operation": operation,
    "result": result
}

with open("Lab03Task01Server.json", "w") as f:
    json.dump(details, f, indent=4)

response = str(result)
c.send(response.encode())
c.close()
s.close()