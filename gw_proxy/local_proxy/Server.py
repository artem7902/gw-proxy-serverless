import ssl
import threading
from http.server import HTTPServer

from gw_proxy.local_proxy.Handle_Request import Handle_Request
from osbot_utils.utils.Http import GET
from osbot_utils.utils.Misc              import random_port


class Server():
    def __init__(self, port=None, target=None, host=None):     # todo: make this random
        self.port     = port
        self.host     = host
        self.target   = target
        self.with_ssl = False
        if self.with_ssl:
            self.scheme   = 'http'
        else:
            self.scheme = 'https'
        self.httpd    = None

    # openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
    def setup(self):
        if self.port   is None: self.port   = random_port()
        if self.host   is None: self.host   = '127.0.0.1'
        if self.target is None: self.target = 'https://httpbin.org'
        Handle_Request.proxy_target = self.target
        self.httpd = HTTPServer((self.host, self.port), Handle_Request)
        if self.with_ssl:
            self.httpd.socket = ssl.wrap_socket(self.httpd.socket, certfile='./server.pem', server_side=True)
        return self

    def start(self):
        self.httpd.serve_forever()

    def start_async(self):
        if self.httpd is None:
            self.setup()
        thread = threading.Thread(target=self.start)
        thread.start()
        return self

    def stop(self):
        self.httpd.shutdown()

    # helper methods
    def local_url(self, path=''):
        return f'{self.scheme}://{self.host}:{self.port}/{path}'

    def target_get(self, path=''):
        url = f'{self.target}/{path}'
        return GET(url)
        
