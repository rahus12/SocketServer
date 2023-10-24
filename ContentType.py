'''
Determining the content type by splitting the request and getting the file extension
eg: .gif, .html etc
The HTTP and MIME specs specify that header lines must end with \r\n
'''
from datetime import datetime
class Type:
    def getContentType(request)->str:
        # print(request.decode())
        return request.decode().split()[1].split('.')[-1]
    
    def setHeader(request):
        response = ""
        content_type = Type.getContentType(request)
        # print (content_type)
        # print(request.decode())
        #text type
        if content_type in ["css","html","js"]:
                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Type: text/" + content_type + "\r\n"                
                
        #images and gif
        elif content_type in ["jpg","jpeg","png","gif"]:
                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Type: image/" + content_type + "\r\n"                
        #video
        elif content_type in ["mp4","mpeg"]:
                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Type: video/" + content_type + "\r\n"
        elif content_type == "/":
                content_type = "html"
                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Type: text/" + content_type + "\r\n" 
                              
        # else:
        #         response = "HTTP/1.1 200 OK\r\n"
        #         response += "Content-Type: text/html\r\n"
                
        # response += "\r\n"
        date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
        response += f"Date: {date}\r\n"

        return response   