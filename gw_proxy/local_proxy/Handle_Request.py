from http.server import BaseHTTPRequestHandler

class Handle_Request(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title> goes here.</title></head>")
        self.wfile.write("<p>You accessed path: {0}</p>".format(self.path).encode())
        self.wfile.write(b"</body></html>")
        print(self.path)