from unittest import TestCase

from gw_proxy.api.Lambda_Event import Lambda_Event


class test_Lambda_Event(TestCase):

    def setUp(self) -> None:
        self.params       = {}
        self.lambda_event = Lambda_Event(self.params)

    # todo: improve test
    def test_ctor(self): 
        self.assertEquals(self.lambda_event.lambda_data    , {'body': {}, 'path': '', 'method': '', 'domain_prefix': None, 'headers': {}})
        self.assertEquals(self.lambda_event.http_proxy.body, {})
