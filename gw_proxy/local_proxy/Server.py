import threading
from http.server import HTTPServer

from gw_proxy.local_proxy.Handle_Request import Handle_Request


class Server():
    def __init__(self, port=12345):     # todo: make this random 
        self.port  = port
        self.httpd = None

    def setup(self):
        server_address = ('127.0.0.1', self.port)
        self.httpd = HTTPServer(server_address, Handle_Request)
        return self

    def start(self):
        self.httpd.serve_forever()

    def start_async(self):
        thread = threading.Thread(target=self.start)
        thread.start()

    def stop(self):
        self.httpd.shutdown()
        
