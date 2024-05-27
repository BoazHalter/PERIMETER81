import http.server
import socketserver
 
PORT = 8000 #The PORT variable defines the port number on which the server will listen (8000 in this case).
DIRECTORY = "." #The DIRECTORY variable specifies the directory from which to serve files (the current directory, .).

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
