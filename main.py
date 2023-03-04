import socket
import requests



i = requests.get('http://httpbin.org/get')
print(i.content)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen()

print("server started")

print(socket.gethostbyname(socket.gethostname()))

user,addres=server.accept()

done=False

print("server started 2 ")

while not False:
    msg = user.recv(1024).decode("utf_8")
    user.send(f"user:{msg}".encode("utf_8"))
    print(msg)

