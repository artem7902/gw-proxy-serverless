from unittest import TestCase

from gw_proxy.api.Http_Proxy import Http_Proxy


class test_Http_Proxy(TestCase):

    def setUp(self):
        self.http_proxy = Http_Proxy(body=None, path=None,headers={},method=None,target=None,)

    def test_ctor(self):
        self.assertIsInstance(self.http_proxy, Http_Proxy)
        self.assertIs(type(self.http_proxy).__name__ , 'Http_Proxy')

    
    def test_bad_request(self):
        self.assertEqual(self.http_proxy.bad_request('el-body'),  {'statusCode': 400, 'body': 'el-body'})

    def test_server_error(self):
        self.assertEqual(self.http_proxy.server_error('el-body'),  {'statusCode': 500, 'body': 'el-body'})

    def test_server_ok(self):
        is_base_64 = False
        headers    = {'an': 'header'}
        body       = 'el-body'

        self.assertEqual(self.http_proxy.ok(headers, body,is_base_64),  {'isBase64Encoded': is_base_64, 'statusCode': 200, 'headers':headers, 'body': 'el-body'})