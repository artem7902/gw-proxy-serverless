from unittest import TestCase, mock
from unittest.mock import patch


from gw_proxy.local_proxy.Handle_Request import Handle_Request
from gw_proxy.local_proxy.Mock_Request import Mock_Request


class test_Handle_Request(TestCase):
    
    @patch.object(Mock_Request,'sendall')
    def test_mock_request_doesnt_work(self, sendall):
        Handle_Request.proxy_target = 'https://httpbin.org/get'
        Handle_Request(request=Mock_Request, client_address=[''], server='').do_GET()
        assert sendall.call_count == 2


