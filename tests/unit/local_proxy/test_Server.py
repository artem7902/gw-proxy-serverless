import json
import threading
import urllib
from time import sleep
from unittest import TestCase

from gw_proxy.local_proxy.Server import Server
from osbot_utils.utils.Http import GET, POST


class test_Server(TestCase):
    def setUp(self) -> None:
        self.server = Server().start_async()

    def tearDown(self) -> None:
        self.server.stop()

    def test_get(self):
        result = GET(f'http://127.0.0.1:{self.server.port}')
        assert "<title>httpbin.org</title>" in result

    def test_get_with_params(self):
        result = json.loads(GET(f'http://127.0.0.1:{self.server.port}/get?a=12'))
        assert result.get('args') == {'a':'12' }

    def test_post(self):
        data       = json.dumps({"aa":"12"})
        headers    = {'Content-Type': 'application/json'}
        raw_result = POST(f'http://127.0.0.1:{self.server.port}/post?a=42', data=data, headers=headers)
        result     = json.loads(raw_result)
        assert result.get('args') == {'a' : '42'}
        assert result.get('data') == '{"aa": "12"}'
        assert result.get('url') == 'https://httpbin.org/post?a=42'





