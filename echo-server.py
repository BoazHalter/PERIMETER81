import http.server
import socketserver
import socket
import requests
import os
import json
from urllib.parse import parse_qs

# Define the port for the HTTP server
PORT = 8080

# Path to the index.html file
INDEX_HTML_PATH = 'index.html'

class FormRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the index.html file
        if self.path == '/':
            if os.path.exists(INDEX_HTML_PATH):
                try:
                    with open(INDEX_HTML_PATH, 'rb') as file:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        self.wfile.write(file.read())
                except Exception as e:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(b'Internal server error: ' + str(e).encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'File not found')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

    def do_POST(self):
        # Handle the form submission
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            post_params = parse_qs(post_data)
            user_input = post_params.get('user_input', [''])[0]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            ip_address = self.get_local_ip()
            geo_location = self.get_geo_location(ip_address)
            response = {
                'user_input': user_input,
                'ip_address': ip_address,
                'geo_location': geo_location
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

    def get_local_ip(self):
        # Try to get the local IP address
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
        except socket.error:
            local_ip = '127.0.0.1'  # Default to localhost if an error occurs
        return local_ip

    def get_geo_location(self, ip_address):
        # Fetch geolocation data using an external service
        try:
            response = requests.get(f'http://ip-api.com/json/{ip_address}')
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': 'Unable to fetch geo location'}
        except Exception as e:
            return {'error': str(e)}

# Set up the HTTP server with the custom request handler
Handler = FormRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
