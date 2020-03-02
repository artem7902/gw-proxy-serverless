import json
from unittest import TestCase
import requests

from gw_proxy.api.Http_Proxy import Http_Proxy


class test_Http_Proxy(TestCase):

    def setUp(self):
        self.http_proxy = Http_Proxy(body=None,headers={},method=None,target=None)

    def test_ctor(self):
        self.assertIsInstance(self.http_proxy, Http_Proxy)
        self.assertIs(type(self.http_proxy).__name__ , 'Http_Proxy')

    def test_bad_request(self):
        self.assertEqual(self.http_proxy.bad_request('el-body'),  {'statusCode': 400, 'headers': {}, 'body': b'el-body'})

    def test_make_request(self):
        http_proxy = Http_Proxy(target='https://postman-echo.com/get?foo1=bar1&foo2=bar2' )

