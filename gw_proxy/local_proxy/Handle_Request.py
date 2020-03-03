import json
from http.server import BaseHTTPRequestHandler

from gw_proxy.api.Http_Proxy import Http_Proxy


class Handle_Request(BaseHTTPRequestHandler):

    proxy_target          = None                 # todo: find a better solution to define the default target
    skip_response_headers = ['content-encoding', 'transfer-encoding', 'transfer-encoding', 'content-length']

    def __init__(self, request, client_address, server):
        if self.proxy_target is None:
            raise Exception('in Handle_Request, proxy_target is not set')
        super().__init__(request, client_address, server)

    def handle(self):                                   # override base method because it was hanging due to "self.close_connection = True"
        self.handle_one_request()

    def handle_response(self, response):
        body        = response.get('body'       )
        headers     = response.get('headers'    )
        status_code = response.get('statusCode' )

        (self.send_status_code     (status_code)
             .send_response_headers(headers    )
             .send_data            (body      ))
        return self

    def send_data(self, data):
        self.wfile.write(data)
        return self

    def send_response_headers(self, headers={}):
        for key,value in headers.items():
            if key.lower() not in self.skip_response_headers:
                self.send_header(key, value)
        self.end_headers()
        return self

    def send_status_code(self, status_code):
        self.send_response(status_code)
        return self

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        target      = f'{self.proxy_target}{self.path}'
        http_proxy  = Http_Proxy(target=target, method='GET', headers=self.headers)
        response    = http_proxy.make_request()
        self.handle_response(response)

    def do_OPTIONS(self):
        target = f'{self.proxy_target}{self.path}'
        http_proxy = Http_Proxy(target=target, method='OPTIONS', headers=self.headers)
        response = http_proxy.make_request()
        self.handle_response(response)
        #asd.asd()

    def do_POST(self):
        """Respond to a POST request."""
        target = f'{self.proxy_target}{self.path}'
        content_len = int(self.headers.get('content-length', 0))
        if content_len > 0:
            post_body = self.rfile.read(content_len)
        else:
            post_body = b''
        http_proxy = Http_Proxy(target=target, method='POST', body=post_body, headers=self.headers)
        response = http_proxy.make_request()
        self.handle_response(response)

    def do_PUT(self):                                       # todo: refactor these methods (do_GET, do_POST, do_PUT) since most have the same code
        """Respond to a PUT request."""
        target = f'{self.proxy_target}{self.path}'
        content_len = int(self.headers.get('content-length', 0))
        if content_len > 0:
            put_body = self.rfile.read(content_len)
        else:
            put_body = b''
        http_proxy = Http_Proxy(target=target, method='PUT', body=post_body, headers=self.headers)
        response = http_proxy.make_request()
        self.handle_response(response)