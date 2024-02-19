#5
import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ['/cgi-bin']

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()