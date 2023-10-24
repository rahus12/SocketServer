'''
Handle the GET requests and send back appropriate responses
Supports file types such as html, js, css, gif, jpg, gif, mp4
Supports error codes such as 200, 400, 403, 404
Supports headers content-type, content-length, date
'''

from ContentType import Type 
import os
import logging
from datetime import datetime

class Handler:
    def getFilePath(request,document_root):
        path = request.decode().split()[1]        
        
        if path == "/" or path == "/index":
            file1 = "index.html"
                        
        else:
            # p = os.getcwd()
            # p = p.replace('\\','/')
            # file1 = p + path
            file1 = document_root + path

        return file1
                
    def handle_client(client_socket,document_root):
        try:
            request = client_socket.recv(2048)            
            header = Type.setHeader(request)
            content_type = Type.getContentType(request)            
            
            file1 = Handler.getFilePath(request,document_root)
           
            
            if not os.path.isfile(file1):
                # code for error 404 - page not found
                if content_type in ["html","css","js","gif","jpg","jpeg","png","gif","mp4","mpeg","/"]:
                    message = "<html><body><h1>404 Not Found</h1></body></html>"                             
                    response = "HTTP/1.1 404 Not Found\r\n"
                    response += "Content-Type: text/html\r\n"
                    response += f"Date: {datetime.now().isoformat()}\r\n"
                    response += f"Content-Length: {str(len(message))}\r\n"
                    response += "\r\n"
                    response += message
                    response = response.encode()
                
                # Code 403 - Forbiden request -- simple example - if url has "/login" then it gives bad request 
                elif file1.find("login"):
                    message = "<html><body><h1>403 Forbiden Request</h1></body></html>"                             
                    response = "HTTP/1.1 403 Forbiden Request\r\n"
                    response += "Content-Type: text/html\r\n"
                    response += f"Date: {datetime.now().isoformat()}\r\n"
                    response += f"Content-Length: {str(len(message))}\r\n"
                    response += "\r\n"
                    response += message
                    response = response.encode()
                
                # 400 error - Bad request - to maintain simplicity, If the GET request does not have a proper file extension then its a bad requeust
                else:
                    message = "<html><body><h1>400 Bad request</h1></body></html>"                             
                    response = "HTTP/1.1 400 Bad Request\r\n"
                    response += "Content-Type: text/html\r\n"
                    response += f"Date: {datetime.now().isoformat()}\r\n"
                    response += f"Content-Length: {str(len(message))}\r\n"
                    response += "\r\n"
                    response += message
                    response = response.encode()

            
            # 200 - OK code
            else:            
                with open(file1, "rb") as file:
                    response = header
                    content = file.read()
                    content_length = str(len(content))                          
                    response += f"Content-Length: {content_length}\r\n"     
                    response += "\r\n"            
                    
                    response = response.encode()
                    response += content

            client_socket.send(response)

        except Exception as e:
            # logging.error(str(e))
            # print(f"Error handling client: {str(e)}")
            pass
            
        finally:            
            client_socket.close()