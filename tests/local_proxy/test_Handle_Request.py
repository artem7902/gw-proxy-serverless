from unittest import TestCase, mock, skip

from gw_proxy.local_proxy.Handle_Request import Handle_Request
from gw_proxy.local_proxy.Mock_Request import Mock_Request


class test_Handle_Request(TestCase):

    # @skip
    # def test_mock_request(self):
    #     with mock.patch.object(Mock_Request, "sendall") as mocked_sendall:
    #         Handle_Request(request=Mock_Request, client_address=[''], server='').do_GET()
    #         print(mocked_sendall.call_count)

    def test_mock_request___http_bin(self):
        handle_request = Handle_Request(request=Mock_Request, client_address=[''], server='')
        #handle_request.do_GET()
        
        #print(sendall)
        #print(handle_request.do_GET())

    # this is not working , see bug https://github.com/filetrust/gw-proxy-serverless/issues/35
    # @mock.patch('Mock_Request.sendall')
    # def test_mock_request_doesnt_work(self, sendall):
    #     Handle_Request(request=Mock_Request, client_address=[''], server='')


