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
SITE_NAME = 'https://send.firefox.com/'
@app.route('/ping')
def ping():
    return 'pong'

@sockets.route('/api/ws')
def echo_socket(ws):                # this all works ok
    print('\n\n********* /api/ws')

    ff_ws = create_connection("wss://send.firefox.com/api/ws")

    file_metadata = ws.receive()
    print("sending file_metadata")
    ff_ws.send(file_metadata)
    target_details = ff_ws.recv()
    print(f'target_details: {target_details}')
    ws.send(target_details)
    bytes_1 = ws.receive()
    bytes_2 = ws.receive()
    bytes_3 = ws.receive()
    #print(f"sending bytes_1 : {len(bytes_1)}")
    ff_ws.send(bytes_1)
    #print(f"sending bytes_2 : {len(bytes_2)}")
    ff_ws.send(bytes_2)
    #print(f"sending bytes_3 : {len(bytes_3)}")
    ff_ws.send(bytes_3)
    result = ff_ws.recv()
    print(f'result: {result}')
    ws.send(result)
    print('<<<< all done >>>>>\n\n')


@sockets.route('/api/ws__ok')
def echo_socket(ws):
    print('********* in Socket')

    message = ws.receive()
    if type(message) is str:
        print(f"received: {message}")
        file_metadata = json.loads(message)
        #print(f"fileMetadata: {message_data.get('fileMetadata')}")
        print('>>>>> sending ok <<<<<<<<<<')
        print(ws.send)
        ws.send('{"url":"https://send.firefox.com/download/8de4acc1dd5bee5a/","ownerToken":"88b28511eb6d5fc2d23f","id":"8de4acc1dd5bee5a"}')
        #         , json=True, namespace='/api/ws')
        print('>>>>> all done')

        #print(Files.save_string_as_file('/tmp/_firefox_send__file_metadata', json.dumps(file_metadata)))
        #print(Files.save_bytes_as_file('/tmp/_firefox_send__bytes_1', ws.receive()))
        #print(Files.save_bytes_as_file('/tmp/_firefox_send__bytes_2', ws.receive()))
        #print(Files.save_bytes_as_file('/tmp/_firefox_send__bytes_3', ws.receive()))

        # while True:
        #     bytes = ws.receive()
        #     print(f'received {len(bytes)}')
        #     print(bytes)
        #     if len(bytes) == 1:
        #         break

            #print(bytes)
            #bytes_2 = ws.receive()
            #bytes_3 = ws.receive()
            ##print(f'received {len(bytes_1)} - {len(bytes_2)} - {len(bytes_3)}')
        # #print(type(ws.receive()),ws.closed)
        # print('>>>>> 1')
        # print(type(ws.receive()), ws.closed)
        # print('>>>>> 2')
        # print(type(ws.receive()), ws.closed)
        # print('>>>>> 3')
        ws.send('{"ok": true}', ws.closed)
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