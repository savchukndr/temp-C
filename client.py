import socket

sock = socket.socket()
sock.connect(('localhost', 1111))
sock.send(b'Hi, its sava')

data = sock.recv(1024)
sock.close()
print(data)