import socket

sock = socket.socket()

sock.bind(('',9090))

sock.listen(3)
print("server is listening in port 9090")
conn, add = sock.accept()
print("server is accepted new client", add)
data = conn.recv(1024)
print("client sent this data", data.decode())
conn.send(data)
conn.close()
sock.close()
