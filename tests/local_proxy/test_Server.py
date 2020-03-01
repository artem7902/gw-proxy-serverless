import threading
import urllib
from time import sleep
from unittest import TestCase

from gw_proxy.local_proxy.Server import Server
from osbot_utils.utils.Http import GET


class test_Server(TestCase):
    def setUp(self) -> None:
        pass

    def test_start(self):
        server = Server()
        server.setup().start_async()
        result = GET(f'http://127.0.0.1:{server.port}')
        self.assertTrue("<html><head><title>" in result)
        server.stop()
        #print('here')
    #
    #     print(server.start)
    #     print(GET('https://127.0.0.1:12345'))


