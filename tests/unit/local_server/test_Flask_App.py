from unittest import TestCase

from gw_proxy.local_server.Flask_App import app as Flask_App


class test_Flask_App(TestCase):

    def test_request__root(self):
        app = Flask_App.test_client()
        response = app.get('/')
        print(response.data)

    def test_request__aaa(self):
        app = Flask_App.test_client()
        response = app.get('/aaa')
        print(response.data)

    def test_request__aaa_POST(self):
        app = Flask_App.test_client()
        response = app.post('/a/frontend/session',json={})
        print(response.data)