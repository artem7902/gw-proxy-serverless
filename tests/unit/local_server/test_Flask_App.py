import threading
from unittest import TestCase

from werkzeug.serving import make_server

from gw_proxy.local_server.Flask_App import app as Flask_App
from osbot_utils.utils.Http import GET
from osbot_utils.utils.Misc import random_port

class ServerThread(threading.Thread):

    def __init__(self, app, port):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('start server')
        self.srv.serve_forever()

    def stop(self):
        print('stopping server')
        self.srv.shutdown()


class test_Flask_App(TestCase):

    # start and stop server
    def test_app__root(self):
        port = random_port()
        url  = f'http://127.0.0.1:{port}'
        server = ServerThread(Flask_App, port)
        server.start()
        #print(GET(f'{url}/ping'))
        print(GET(f'{url}/wp-content/uploads/2019/11/Header-Image-scaled.jpg'))

        #print('\n\n**** server should be live****')
        server.stop()
        # server = make_server(host='127.0.0.1', port=port, app=Flask_App)
        # thread = threading.Thread(server.serve_forever)
        # thread.start()
        # print(server)
        # thread = threading.Thread(target=Flask_App.run,args={'debug':False, 'port':random_port()})
        # thread.start()
        # #server = Flask_App.run()
        # print('here')
        # from flask import request
        # print(request.environ['werkzeug.server.shutdown'])
        # print('after stop')
        #from time import sleep
        #sleep(5)

    # simulate requests
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