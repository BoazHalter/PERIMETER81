import http.server
import socketserver
import socket
import requests
import os
import json

# Define the port for the HTTP server
PORT = 8080

# Echo message passed to the script
ECHO_MESSAGE = os.getenv('ECHO_MESSAGE', "Hello, World!")

# Environment variable (e.g., 'staging' or 'production')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Path to the index.html file
INDEX_HTML_PATH = './index.html'

class EchoRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/index.html':
            if os.path.exists(INDEX_HTML_PATH):
                ip_address = self.get_local_ip()
                geo_location = self.get_geo_location(ip_address)
                geo_location_str = json.dumps(geo_location, indent=4)
                with open(INDEX_HTML_PATH, 'r') as file:
                    content = file.read()
                    updated_content = content.replace('{{ECHO_MESSAGE}}', ECHO_MESSAGE)
                    updated_content = updated_content.replace('{{GEO_LOCATION}}', geo_location_str)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(updated_content.encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'File not found')
        elif self.path == '/echo':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            ip_address = self.get_local_ip()
            geo_location = self.get_geo_location(ip_address)
            response = {
                'message': ECHO_MESSAGE,
                'environment': ENVIRONMENT,
                'ip_address': ip_address,
                'geo_location': geo_location
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

    def get_local_ip(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip

    def get_geo_location(self, ip_address):
        try:
            response = requests.get(f'http://ip-api.com/json/{ip_address}')
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': 'Unable to fetch geo location'}
        except Exception as e:
            return {'error': str(e)}

Handler = EchoRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
