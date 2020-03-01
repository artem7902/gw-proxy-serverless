from unittest import TestCase

from gw_proxy.local_proxy.Server import Server
from osbot_utils.utils.Http      import GET


class test_Server(TestCase):


    def test_httpbin_org(self):
        server = Server().start_async()
        result = GET(server.url())
        assert "<title>httpbin.org</title>" in result
        server.stop()

    def test_glasswall_solutions_com(self):
        server = Server(target='https://glasswallsolutions.com').start_async()
        result = GET(server.url())
        assert "<title>Unparalleled Protection from Advanced Persistent Threats (APT)</title>" in result
        server.stop()


    # def setUpClass(cls) -> None:
    #     print('in setUpClass')
    #     pass
    #
    # def tearDownClass(cls) -> None:
    #     print('in tearDownClass')
    #     pass
