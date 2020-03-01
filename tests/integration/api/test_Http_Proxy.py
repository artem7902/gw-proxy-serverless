import json
from unittest import TestCase

from gw_proxy.api.Http_Proxy import Http_Proxy


class test_Http_Proxy(TestCase):

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
        self.assertEqual(body.get('data'), 'some=data')

    def test_server_error(self):
        self.assertEqual(Http_Proxy().server_error('el-body'),  {'statusCode': 500, 'headers': {}, 'body': 'el-body'})

    def test_server_ok(self):
        is_base_64 = False
        headers    = {'an': 'header'}
        body       = 'el-body'

        self.assertEqual(Http_Proxy().ok(headers, body,is_base_64),  {'isBase64Encoded': is_base_64, 'statusCode': 200, 'headers':headers, 'body': 'el-body'})