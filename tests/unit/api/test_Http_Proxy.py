import json
from unittest import TestCase

from gw_proxy.api.Http_Proxy import Http_Proxy


class test_Http_Proxy(TestCase):

    def setUp(self):
        self.http_proxy = Http_Proxy(body=None,headers={},method=None,target=None)

    def test_ctor(self):
        self.assertIsInstance(self.http_proxy, Http_Proxy)
        self.assertIs(type(self.http_proxy).__name__ , 'Http_Proxy')

    def test_bad_request(self):
        self.assertEqual(self.http_proxy.bad_request('el-body'),  {'statusCode': 400, 'body': 'el-body'})

    def test_make_request(self):
        http_proxy = Http_Proxy(target='https://postman-echo.com/get?foo1=bar1&foo2=bar2' )

    # todo, move to integration tests

    def test_request_get__glasswall(self):
        target = 'https://glasswallsolutions.com/asd'
        http_proxy = Http_Proxy(target=target, method='GET')
        body = http_proxy.request_get().get('body')
        print(type(body))


    def test_request_get__postman_echo(self):
        target = 'https://postman-echo.com/get?foo1=bar1&foo2=bar2'
        http_proxy = Http_Proxy(target=target, method='GET')
        body = http_proxy.request_get().get('body')
        self.assertEqual(body, b'{"args":{"foo1":"bar1","foo2":"bar2"},"headers":{"x-forwarded-proto":"https","host":"postman-echo.com","accept":"*/*","accept-encoding":"identity","x-forwarded-port":"443"},"url":"https://postman-echo.com/get?foo1=bar1&foo2=bar2"}')

    # todo, move to integration tests
    def test_request_post__postman_echo(self):
        target     = 'https://postman-echo.com/post?foo1=bar1&foo2=bar2'
        data       = {'some':'data'}
        headers    = {'Content-Type': 'application/json'}
        http_proxy = Http_Proxy(target=target, method='POST', body=data, headers=headers)
        body       = json.loads(http_proxy.request_post().get('body'))
        self.assertEqual(body.get('args'), {'foo1': 'bar1', 'foo2': 'bar2'})
        self.assertEqual(body.get('data'), data)

    def test_server_error(self):
        self.assertEqual(self.http_proxy.server_error('el-body'),  {'statusCode': 500, 'body': 'el-body'})

    def test_server_ok(self):
        is_base_64 = False
        headers    = {'an': 'header'}
        body       = 'el-body'

        self.assertEqual(self.http_proxy.ok(headers, body,is_base_64),  {'isBase64Encoded': is_base_64, 'statusCode': 200, 'headers':headers, 'body': 'el-body'})