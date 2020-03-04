import json
import sys

from websocket import create_connection

sys.path.append('.')
sys.path.append('./modules/OSBot-Utils')

from osbot_utils.utils.Files import Files
from flask import Flask,request,redirect,Response
#from flask_socketio import SocketIO, emit
import requests

from gw_proxy.api.Http_Proxy import Http_Proxy

from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

#socketio = SocketIO(app)

SITE_NAME = 'https://glasswallsolutions.com/'
SITE_NAME = 'https://demo.pydio.com/'
#SITE_NAME = 'https://httpbin.org'

#demo.pydio websockets

@sockets.route('/ws/event')
def echo_socket(ws):                # this all works ok
    print('\n\n********* /ws/event')
    #ff_ws = create_connection("wss://send.firefox.com/api/ws")
    ##file_metadata =
    #print("sending file_metadata")
    data = ws.receive()
    print(f'received: {data}')
    print('>>>>> all done <<<<< \n')

    while not ws.closed:
        message = ws.receive()
        print(f'********** received more data: {message} ************')

@app.route('/')
@app.route('/<path:path>',methods=['GET','POST',"PUT","DELETE"])
def proxy(path=''):
    global SITE_NAME
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection','host']
    try:
        #print(request.headers)
        target= f'{SITE_NAME}{path}'
        if request.method=='GET':
            response = Http_Proxy(target=target,method='GET',headers=request.headers).make_request()
            return Response(response.get('body'), response.get('statusCode'),response.get('headers'))


        elif request.method=='POST':
            
            response = Http_Proxy(target=target, method='POST', headers=request.headers,body=request.data).make_request()
            #print(response)
            return Response(response.get('body'), response.get('statusCode'), response.get('headers'))

            # headers = {}
            # for (key,value) in request.headers:
            #     if key.lower() != 'host':
            #         headers[key] = value
            # #print(headers)
            # #print('content type: ', request.headers.get('Content-Type'))
            # if request.headers.get('Content-Type')== 'application/json':
            #     print('POST : ', request.get_json())
            #     resp = requests.post(f'{SITE_NAME}{path}',json=request.get_json(), headers=headers)
            # else:
            #     resp = requests.post(f'{SITE_NAME}{path}', data=request.get_data(), headers=headers)
            # headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            # response = Response(resp.content, resp.status_code, headers)
            # return response
        elif request.method=='PUT':
            headers = {}
            for (key,value) in request.headers:
                if key.lower() != 'host':
                    headers[key] = value
            #print(headers)
            #print('content type: ', request.headers.get('Content-Type'))
            if request.headers.get('Content-Type')== 'application/json':
                #print('PUT : ', request.get_json())
                resp = requests.put(f'{SITE_NAME}{path}',json=request.get_json(), headers=headers)
            else:
                resp = requests.post(f'{SITE_NAME}{path}', data=request.get_data(), headers=headers)
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
        elif request.method=='DELETE':
            resp = requests.delete(f'{SITE_NAME}{path}').content
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
    except Exception as error:
        return f'{error}'

if __name__ == '__main__':
    #app.run(debug = True,port=12345)#, ssl_context='adhoc')
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    print('Starting Flask server with WebSocket support')
    server = pywsgi.WSGIServer(('', 12345), app, handler_class=WebSocketHandler)
    server.serve_forever()