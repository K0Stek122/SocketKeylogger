import socket
import sys

IP = socket.gethostname()
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen(5)

output = None

for i in range(len(sys.argv)):
    try:
        if sys.argv[i] == "-o" or sys.argv[i] == "--output":
            output = sys.argv[i+1]
    except IndexError:
        print("Wrong Usage, continuing without arguments")

clientSocket, clientAddy = s.accept()
if output: f = open(output, "a")

while True:
    msg = clientSocket.recv(24)
    if msg:
        print(msg.decode("utf-8"))
        if output:
            f.write(msg.decode("utf-8") + " | ")
    else:
        print("CONNECTION CLOSED")
        break

s.close()
if output: f.close()
