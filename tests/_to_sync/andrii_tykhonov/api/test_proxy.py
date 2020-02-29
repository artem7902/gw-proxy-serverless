from http import HTTPStatus
from unittest import mock, TestCase

from pbx_gs_python_utils.utils.Http import GET

from gw_proxy._to_sync.andrii_tykhonov.api.Response_Handler import Response_Handler
from gw_proxy._to_sync.andrii_tykhonov.api.proxy import Proxy


class test_proxy(TestCase):

    def setUp(self):
        self.proxy = Proxy('http://example.com')
        self.result = None
        self.png_data = None

    @mock.patch('requests.get')
    def test_handle_response(self, mockget):
        headers = { 'Content-Type': 'text'}
        attrs = {'headers.return_value': headers}
        response = mock.Mock(**attrs)
        response.headers = headers
        # response.content = b'test content'
        response.text = b'test content'
        mockget.return_value = response

        resp = self.proxy.handle_request({})

        assert resp['isBase64Encoded'] == False
        assert resp['statusCode'] == HTTPStatus.OK.value
        assert resp['headers']['Content-Type'] ==  'text'
        assert b'test content' in resp['body']

    @mock.patch('requests.get')
    def test_handle_binary_response(self, mockget):
        headers = {
            'Content-Type': 'image/png',
        }
        attrs = {'headers.return_value': headers}
        response = mock.Mock(**attrs)
        response.headers = headers
        response.content = b'test content'
        mockget.return_value = response

        resp = self.proxy.handle_request({'headers': headers})

        assert resp['isBase64Encoded'] == True
        assert resp['statusCode'] == HTTPStatus.OK.value
        assert resp['headers']['Content-Type'] ==  'image/png'

    @mock.patch('requests.get')
    def test_internal_server_error(self, mockget):
        mockget.side_effect = Exception('proxy error')

        resp = self.proxy.handle_request({})

        assert resp['isBase64Encoded'] == False
        assert resp['statusCode'] == HTTPStatus.INTERNAL_SERVER_ERROR.value
        assert resp['body'] == 'Proxy error: proxy error'

    @mock.patch('requests.get')
    def test_log_request(self, mockget):
        headers = {
            'Content-Type': 'text/html; charset=UTF-8',
        }
        self.proxy.log_request = mock.Mock()

        resp = self.proxy.handle_request({
            'path': '/path',
            'httpMethod': 'GET',
            'headers': headers,
            'requestContext': {
                'domainPrefix': 'prefix',
            },
        })

        self.proxy.log_request.assert_called_once_with(
            '/path', 'GET', headers, 'prefix', 'http://example.com')