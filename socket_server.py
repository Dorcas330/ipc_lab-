import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)
print("Socket Server listening on port 5000...")

conn, addr = server.accept()
data = conn.recv(1024).decode()
print(f"Received from client: {data}")

conn.sendall("Hello World from Socket Server!".encode())
conn.close()