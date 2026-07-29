import http.server
import socketserver
import os

PORT = 6005
DIRECTORY = '/home/thameem7185/ hello'

if os.path.exists(DIRECTORY):
    os.chdir(DIRECTORY)
else:
    print(f"Error: Directory '{DIRECTORY}' does not exist.")
    exit(1)

# Custom handler to serve nexus.html by default
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/nexus.html'
        return super().do_GET()

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving {DIRECTORY}/nexus.html at port {PORT}")
    print(f"Open your browser and go to http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()