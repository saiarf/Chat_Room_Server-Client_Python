# echo_server.py
import time, socket

print("\nWelcome to Chat Rooms")
print("Initialising....\n")
time.sleep(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1234
s.bind((host, port))
print(host, "(", port, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nType E and then press enter to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "E":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)