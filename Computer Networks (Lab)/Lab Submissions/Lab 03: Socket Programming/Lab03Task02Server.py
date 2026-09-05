import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',9999))
print("Socket successfully created and bound to port 9999")
s.listen(5)
print("Server is listening on port 9999...")

c,address = s.accept()
print("Got connection from", address)

message = c.recv(1024).decode()

grade_point = float(message)
if grade_point == 4.33:
    grade = "A+"
    qualification = "Excellent"

elif grade_point == 4.00:
    grade = "A"
    qualification = "Excellent"

elif grade_point == 3.66:
    grade = "A-"
    qualification = "Very good"

elif grade_point == 3.33:
    grade = "B+"
    qualification = "Very good"

elif grade_point == 3.00:
    grade = "B"
    qualification = "Very good"

elif grade_point == 2.66:
    grade = "B-"
    qualification = "Good"

elif grade_point == 2.33:
    grade = "C+"
    qualification = "Good"

elif grade_point == 2.00:
    grade = "C"
    qualification = "Good"

elif grade_point == 1.66:
    grade = "C-"
    qualification = "Passable"

elif grade_point == 1.33:
    grade = "D+"
    qualification = "Passable"

elif grade_point == 1.00:
    grade = "D"
    qualification = "Passable"

elif grade_point == 0.00:
    grade = "E"
    qualification = "Failure"

else:
    grade = "Invalid"
    qualification = "Invalid grade point"


response = f"Grade: {grade}, Qualification: {qualification}"
c.send(response.encode())
c.close()
s.close()
