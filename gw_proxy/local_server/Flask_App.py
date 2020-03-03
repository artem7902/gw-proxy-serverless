import json
import sys
sys.path.append('.')

from flask import Flask,request,redirect,Response
from flask_socketio import SocketIO, emit
import requests

from gw_proxy.api.Http_Proxy import Http_Proxy

from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

#socketio = SocketIO(app)

SITE_NAME = 'https://glasswallsolutions.com/'
SITE_NAME = 'https://demo.pydio.com/'
#SITE_NAME = 'https://httpbin.org'
SITE_NAME = 'https://send.firefox.com/'
@app.route('/ping')
def ping():
    return 'pong'

@sockets.route('/api/ws')
def echo_socket(ws):
    print('********* in Socket')

    message = ws.receive()
    if type(message) is str:
        print(f"received: {message}")
        message_data = json.loads(message)
        #print(f"fileMetadata: {message_data.get('fileMetadata')}")
        print('>>>>> sending ok <<<<<<<<<<')
        print(ws.send)
#        ws.send("{'ok-1': True}")
#        ws.send("{ok_1: true }")
#        ws.send("{'ok-2': True}")
        # print('>>>>> sending url')
        ws.send('{"url":"https://send.firefox.com/download/8de4acc1dd5bee5a/","ownerToken":"88b28511eb6d5fc2d23f","id":"8de4acc1dd5bee5a"}')
        #         , json=True, namespace='/api/ws')
        print('>>>>> all done')


        print(type(ws.receive()),ws.closed)
        print('>>>>> 1')
        print(type(ws.receive()), ws.closed)
        print('>>>>> 2')
        print(type(ws.receive()), ws.closed)
        print('>>>>> 3')
        ws.send('{"ok": true}')
        print('>>>>> 4')


    else:
        print(f"received non string: {type(message)}")
    
    #
    #while not ws.closed:
    #    message = ws.receive()
    #    if not message:
    #        message = ''
    #    print(f'**** received file with size : {len(message)} ')
    #    ws.send({'ok-2': True}, json=True)
    #    ws.send({'ok': True}, json=True, namespace='/api/ws')

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
    #app.run(debug = False,port=443, ssl_context='adhoc')
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    print('starting server')
    server = pywsgi.WSGIServer(('', 12345), app, handler_class=WebSocketHandler)
    server.serve_forever()