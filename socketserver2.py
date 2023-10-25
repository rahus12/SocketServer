'''
Server functionality using sockets
Multi-threaded approach.
Main function

to-do: support arg passing through command line
'''

import socket
import threading
from handler import Handler
import argparse

def main():
    h_client = Handler.handle_client

    parser = argparse.ArgumentParser()
    parser.add_argument("--document_root",type=str,help="your document root")
    parser.add_argument("--port",type=int,help="port number")

    args = parser.parse_args()

    host = "0.0.0.0"
    port = args.port
    document_root = args.document_root
    # port = 8082
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_sock, addr = server.accept()
        
        if client_sock:            
            client_sock.settimeout(15)
            client_thread = threading.Thread(target=h_client, args=(client_sock,document_root))
            client_thread.start()

if __name__ == "__main__":
    main()  