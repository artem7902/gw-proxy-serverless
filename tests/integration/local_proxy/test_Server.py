from unittest import TestCase

from gw_proxy.local_proxy.Server import Server
from osbot_utils.utils.Http import GET, POST, OPTIONS


class test_Server(TestCase):


    def test_httpbin_org__GET(self):
        server = Server().start_async()
        result = GET(server.url())
        assert "<title>httpbin.org</title>" in result
        server.stop()

    def test_httpbin_org__OPTIONS(self):
        server = Server().start_async()
        result = OPTIONS(server.url())
        print(result)
        #assert "<h1>Method Not Allowed</h1>" in result
        server.stop()

    def test_httpbin_org__POST(self):
        server = Server().start_async()
        result = POST(server.url())
        assert "<h1>Method Not Allowed</h1>" in result
        server.stop()

    def test_glasswall_solutions_com__GET(self):
        server = Server(target='https://glasswallsolutions.com').start_async()
        result = GET(server.url())
        assert "<title>Unparalleled Protection from Advanced Persistent Threats (APT)</title>" in result
        server.stop()

