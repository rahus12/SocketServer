import socket
import threading
from handler import Handler



host = "0.0.0.0"
port = 8083

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"Server listening on {host}:{port}")

while True:
    client_sock, addr = server.accept()
    if client_sock:            
        client_sock.settimeout(15)
        Handler.handle_client(client_sock)
    


    
