import socket

sock = socket.socket()
sock.bind(('', 1111))
sock.listen(1)
conn, addr = sock.accept()

print('connected: ', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break
	data = str(data)
	data = list(data)
	data = str(data)
	conn.send(data)

	conn.close()