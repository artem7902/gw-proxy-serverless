import json
import sys


sys.path.append('.')
sys.path.append('./modules/OSBot-Utils')
from osbot_utils.utils.Http import GET
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
SITE_NAME = "https://gofile.io/"

@app.route('/getServer')
def getServer():
    key = request.args.get('c')
    target_url = f'https://apiv2.gofile.io/getServer?c={key}'
    print(target_url)
    result     = GET(target_url)
    server     = json.loads(result).get('data').get('server')
    fixed_data= f'{{"status": "ok", "data": {{"server": "localhost/download?server={server}&params=" }} }}'
    headers = {'content-type': 'application/json; charset=utf-8', 'status': 200}
    return Response(fixed_data, 201, headers)

@app.route('/verifToken')
@app.route('/.gofile.io/verifToken')
def verifToken():
    token = request.args.get('token')
    target_url = f'https://apiv2.gofile.io/verifToken?token={token}'
    data       = GET(target_url)
    headers = {'content-type': 'application/json; charset=utf-8', 'status': 200}
    return Response(data, 201, headers)

@app.route('/.gofile.io/getUploadsList')
def getUploadsList():
    token = request.args.get('token')
    target_url = f'https://apiv2.gofile.io/getUploadsList?token={token}'
    data       = GET(target_url)
    headers = {'content-type': 'application/json; charset=utf-8', 'status': 200}
    return Response(data, 201, headers)

@app.route('/.gofile.io/getServer')
def get_server():
    data = '{"status":"ok","data":{"server":"localhost:443/"}}'
    headers = {'content-type':'application/json; charset=utf-8' , 'status': 200}
    return Response(data, 200, headers)

@app.route('/.gofile.io/upload', methods=['POST'])
def upload():
    headers = {'content-type': 'application/json; charset=utf-8', 'status': 200}
    try:
        # print('>>>>>> in UPLOAD <<<<<<')
        # print(request.get_data())
        # print('>>>>>> request.files <<<<<<')
        # print(request.files['filesUploaded'])
        # print('>>>>>> len(request.files) <<<<<<')
        # print(request.files.getlist('filesUploaded'))
        #print(request.files.items())
        for key,value in request.headers.items():
            print(key,value)
        print('---------------')
        print(request.get_data())

        # target_Folder = Files.folder_create('/tmp/uploaded_files')
        # for file in request.files.getlist('filesUploaded'):
        #     print('--------------')
        #     print(file.filename)
        #     temp_file = f'{target_Folder}/{file.filename}'
        #     print(temp_file)
        #     print(file.save(temp_file))
        # #print(request.files[0])
        data = '{"status":"ok","data":{"code":"nOx5QC","removalCode":"....."}}'
        return Response(data, 200, headers)
    except Exception as error:
        data = f'{{"status":"error", "data": "{error}"}}'
        print(data)
        return Response(data, 200, headers)


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
            #print(f'in POST: {request.get_data()}')
            #from osbot_utils.utils.Dev import Dev
            #Dev.pprint(request.headers)
            response = Http_Proxy(target=target, method='POST', headers=request.headers,body=request.get_data()).make_request()
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
    #app.run(debug = True,port=12345,ssl_context=('cert.pem', 'key.pem'))
    app.run(debug=True, port=443, ssl_context=('localhost.crt', 'localhost.key'))
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    #
    # print('Starting Flask server with WebSocket support')
    # server = pywsgi.WSGIServer(('', 12345), app, handler_class=WebSocketHandler)
    # server.serve_forever()

    # cert created with: openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

    # from https://letsencrypt.org/docs/certificates-for-localhost/
    # openssl req -x509 -out localhost.crt -keyout localhost.key \
    #   -newkey rsa:2048 -nodes -sha256 \
    #   -subj '/CN=localhost' -extensions EXT -config <( \
    #    printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")