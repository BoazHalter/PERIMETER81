import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "."

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Read the HTML file
            with open("index.html", "r") as file:
                html_content = file.read()

            # Get the environment variable
            environment_value = os.getenv('ENVIRONMENT', 'Environment variable not set')
            server_ip = os.getenv('ECHO_SERVER_ECHO_SERVER_PORT_8080_TCP_ADDR','TCP_ADDR not set')
            client_ip = self.client_address[0]
            # Inject the environment variable into the HTML content
            modified_html_content = html_content.replace(
                '</body>',
                f'<div>Environment: {environment_value}</div></body>'
                f'<div>Server IP: {server_ip}</div></body>'
                f'<div>Client IP: {client_ip}</div></body>'
            )

            # Send the modified HTML content
            self.wfile.write(modified_html_content.encode())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
