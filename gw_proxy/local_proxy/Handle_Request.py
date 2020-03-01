import json
from http.server import BaseHTTPRequestHandler

from gw_proxy.api.Http_Proxy import Http_Proxy


class Handle_Request(BaseHTTPRequestHandler):

    def __init__(self, *args, **kvargs):
        self.default_target = 'https://glasswallsolutions.com/'
        #self.default_target = 'http://httpbin.org/'
        super().__init__(*args, **kvargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        try:
            target     = self.default_target + self.path
            http_proxy = Http_Proxy(target=target, method='GET', headers=self.headers)
            response   = http_proxy.make_request()
            body       = response.get('body')
            headers    = response.get('headers')
            self.send_response(200)
            for key,value in headers.items():
                if key != 'Transfer-Encoding':
                    self.send_header(key, value)
                    print(key,value)
            self.end_headers()

            self.wfile.write(body)
        finally:
            self.finish()