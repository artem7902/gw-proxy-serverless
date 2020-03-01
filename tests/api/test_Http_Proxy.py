from unittest import TestCase

from gw_proxy.api.Http_Proxy import Http_Proxy


class test_Http_Proxy(TestCase):

    def setUp(self):
        self.http_proxy = Http_Proxy()

    def test_ctor(self):
        self.assertIsInstance(self.http_proxy, Http_Proxy)
        self.assertIs(type(self.http_proxy).__name__ , 'Http_Proxy')

    # todo improve test
    def test_handle_lambda_event(self):
        event_data = {}
        self.http_proxy.handle_lambda_event(event_data)
        self.assertEquals(self.http_proxy.lambda_event , {'body': {}, 'path': '', 'method': '', 'domain_prefix': None, 'headers': {}, 'request_headers': {'accept': None, 'User-Agent': None, 'accept-encoding': None}})
