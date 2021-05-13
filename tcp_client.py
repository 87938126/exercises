import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect(('Server IP address', port))
print(s.recv(1024).decode())
s.close()
