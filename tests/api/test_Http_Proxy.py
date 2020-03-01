from unittest import TestCase

from gw_proxy.api.Http_Proxy import Http_Proxy


class test_Http_Proxy(TestCase):

    def setUp(self):
        self.http_proxy = Http_Proxy(body=None, path=None,headers={},method=None,target=None,)

    def test_ctor(self):
        self.assertIsInstance(self.http_proxy, Http_Proxy)
        self.assertIs(type(self.http_proxy).__name__ , 'Http_Proxy')