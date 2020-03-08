import http.server
import socketserver

PORT = 8008

handle = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handle) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()