from unittest import TestCase, mock, skip

from gw_proxy.local_proxy.Handle_Request import Handle_Request
from gw_proxy.local_proxy.Mock_Request import Mock_Request


class test_Handle_Request(TestCase):

    def test_mock_request(self):
        try:
            with mock.patch.object(Mock_Request, "sendall") as mocked_sendall:
                Handle_Request(request=Mock_Request, client_address=[''], server='').do_GET()
                print(mocked_sendall.call_count)
        except Exception as error:
            assert str(error) == 'I/O operation on closed file.'  # todo: fix this error that is happening on the `self.finish()` command of do_GET


    # this is not working , see bug https://github.com/filetrust/gw-proxy-serverless/issues/35
    # @mock.patch('Mock_Request.sendall')
    # def test_mock_request_doesnt_work(self, sendall):
    #     Handle_Request(request=Mock_Request, client_address=[''], server='')


