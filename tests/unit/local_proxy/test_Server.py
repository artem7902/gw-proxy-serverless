import threading
import urllib
from time import sleep
from unittest import TestCase

from gw_proxy.local_proxy.Server import Server
from osbot_utils.utils.Http import GET


class test_Server(TestCase):
    def setUp(self) -> None:
        self.server = Server().start_async()

    def tearDown(self) -> None:
        self.server.stop()

    def test_start(self):
        result = GET(f'http://127.0.0.1:{self.server.port}')
        assert "<title>httpbin.org</title>" in result




