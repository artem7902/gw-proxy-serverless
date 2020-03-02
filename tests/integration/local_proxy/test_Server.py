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

    def test_project_send(self):
        server = Server(target='https://www.projectsend.org').start_async()
        result = GET(server.url())
        assert '<title>Access denied | www.projectsend.org used Cloudflare to restrict access</title>' in result
        server.stop()


    def test_gofile_io__file(self):
        target    = 'https://srv-file7.gofile.io'
        server    = Server(target=target).start_async()
        path_file =  'download/OKf7PF/task.png'
        url_file  = f'{server.url()}{path_file}'
        result = GET(url_file,encoding=None)

        tmp_file = '/tmp/temp_image.png'
        with open(tmp_file, 'wb') as file:
            file.write(result)
        print(len(result))
        server.stop()



