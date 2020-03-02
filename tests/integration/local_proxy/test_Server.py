import json
from unittest import TestCase

from gw_proxy.local_proxy.Server import Server
from gw_proxy.local_proxy.Temp_Server import Temp_Server
from osbot_utils.utils.Http import GET, POST, OPTIONS


class test_Server(TestCase):

    def test_httpbin_org__GET(self):
        with Temp_Server() as server:
            assert "<title>httpbin.org</title>" in GET(server.url())

    def test_httpbin_org__OPTIONS(self):
        server = Server().start_async()
        result = OPTIONS(server.local_url())
        print(result)
        #assert "<h1>Method Not Allowed</h1>" in result
        server.stop()

    def test_httpbin_org__POST(self):
        with Temp_Server('https://httpbin.org') as server:
            result = json.loads(POST(f'{server.url()}/post?query=abc','aaa=123'))
            assert result.get('args') == {'query': 'abc'}
            assert result.get('form') == {'aaa': '123'}
            print(result)
            #assert "<h1>Method Not Allowed</h1>" in POST(server.url())


    def test_glasswall_solutions_com__GET(self):
        with Temp_Server('https://glasswallsolutions.com') as server:
            assert "<title>Unparalleled Protection from Advanced Persistent Threats (APT)</title>" in GET(server.url())

    def test_project_send(self):
        server = Server(target='https://www.projectsend.org').start_async()
        result = GET(server.local_url())
        assert '<title>Access denied | www.projectsend.org used Cloudflare to restrict access</title>' in result
        server.stop()

    def test_(self):
        with Temp_Server('https://demo.pydio.com') as server:
            print(server.target)
            print(server.local_url())
            print(server.target_get())


    # def test_gofile_io__file(self):
    #     target    = 'https://srv-file7.gofile.io'
    #     server    = Server(target=target).start_async()
    #     path_file =  'download/OKf7PF/task.png'
    #     url_file  = f'{server.url()}{path_file}'
    #     result = GET(url_file,encoding=None)
    #     print(result)
    #     tmp_file = '/tmp/temp_image.png'
    #     with open(tmp_file, 'wb') as file:
    #         file.write(result)
    #     print(len(result))
    #     server.stop()


    def test_docker_own_cloud__POST(self):
        target = 'http://localhost:8080'
        post_data = 'redirect_url=%252Fapps%252Ffiles%252F%253Fdir%253D%252F%2526fileid%253D3&user=aaaa&password=bbbb&timezone-offset=0&timezone=Europe%2FLondon&requesttoken=JyFNEAkcJSAicnktfQsyP0E5E1oDAA0LegNCeWElaRY%3D%3AJYbeLZUqnE7uNaWsvlE%2BlolO7i5H0J8yUsiRcAnt9rA%3D'
        server = Server(target=target).start_async()
        path_file = 'login'
        result = POST(f'{server.local_url()}{path_file}/login', post_data)
        #print(result)
        #assert "<h1>Method Not Allowed</h1>" in result
        server.stop()


