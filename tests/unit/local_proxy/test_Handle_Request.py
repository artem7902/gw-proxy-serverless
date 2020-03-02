from unittest import TestCase, mock
from unittest.mock import patch


from gw_proxy.local_proxy.Handle_Request import Handle_Request
from gw_proxy.local_proxy.Mock_Request import Mock_Request


class test_Handle_Request(TestCase):

    @patch.object(Mock_Request,'sendall')
    def test_do_GET(self, sendall): 
        Handle_Request.proxy_target = 'https://httpbin.org/get'
        Handle_Request(request=Mock_Request, client_address=[''], server='').do_GET()
        assert sendall.call_count == 2

    def test_do_OPTIONS(self):
        Handle_Request.proxy_target = 'https://httpbin.org/get'
        Handle_Request(request=Mock_Request, client_address=[''], server='').do_OPTIONS()
        #assert sendall.call_count == 2


    @patch.object(Mock_Request, 'sendall')
    def test_do_POST(self,sendall):
        Handle_Request.proxy_target = 'https://httpbin.org'
        handle_request = Handle_Request(request=Mock_Request, client_address=[''], server='')
        handle_request.path='/post'
        handle_request.do_POST()
        assert sendall.call_count == 2


