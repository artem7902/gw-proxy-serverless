import json
import sys
import urllib3

sys.path.append('.')
sys.path.append('./modules/OSBot-Utils')

from gw_proxy.gw.GW_Rebuild_Azure import GW_Rebuild_Azure
from osbot_utils.utils.Http import GET, GET_Json
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

@app.route('/download')
def download():
    headers = {'content-type': 'application/json; charset=utf-8', 'status': 200}
    server_name = request.args.get('server')
    params      = request.args.get('params')
    file_id     = request.args.get('c')
#download?server=srv-file4&params=.gofile.io/getUpload&c=KLURWK
    url = f'https://{server_name}{params}?c={file_id}'
    data = GET(url)
    #print(data)
    return Response(data, 201, headers)

@app.route('/getServer')
def getServer():
    key = request.args.get('c')
    target_url = f'https://apiv2.gofile.io/getServer?c={key}'
    #print(target_url)
    result     = GET(target_url)
    server     = json.loads(result).get('data').get('server')
    fixed_data= f'{{"status": "ok", "data": {{"server": "glasswall.gofile.io/download?server={server}&params=" }} }}'
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
    data = '{"status":"ok","data":{"server":"glasswall.gofile.io:443/"}}'
    headers = {'content-type':'application/json; charset=utf-8' , 'status': 200}
    return Response(data, 200, headers)

@app.route('/.gofile.io/upload', methods=['POST'])
def upload():

    def save_to_gofile(files_to_save):
        server_name = GET_Json('https://apiv2.gofile.io/getServer').get('data').get('server')
        upload_url = f'https://{server_name}.gofile.io/upload'
        multipart_form_data = None
        for file_name, content_type, file_path in files_to_save:
            print(f">>>> Uploading file to gofile server: {file_name}")
            if multipart_form_data is None:
                multipart_form_data = (('filesUploaded', (file_name, open(file_path, 'rb') ,content_type)),)
            else:
                multipart_form_data = (*multipart_form_data, ('filesUploaded', (file_name, open(file_path, 'rb'),content_type)))

        #print(multipart_form_data)
        urllib3.disable_warnings()
        verify_SSL = False          #todo: figure out why this isn't working (note: currenly running server as root due to need to open server in port 443)
        response = requests.post(upload_url, files=multipart_form_data, verify=verify_SSL)
        result   = response.content
        print(f">>>> {result}")
        return result

    def rebuild_files(targets):
        gw_azure = GW_Rebuild_Azure()
        rebuilds = []
        for file_name, content_type, file_path in targets:
            print(f'\n########## Rebuilding file: {file_name}')
            bytes = gw_azure.file_protect(file_path)
            if len(bytes) > 0:
                rebuilt_file = Files.save_bytes_as_file(bytes)
                print(f'########## File rebuild ok\n\n')
                rebuilds.append((file_name, content_type, rebuilt_file))
            else:
                print(f'########## File NOT rebuilt, using original \n')
                rebuilds.append((file_name, content_type, file_path))
        return rebuilds

    headers = {'content-type': 'application/json; charset=utf-8', 'status': 200}
    try:
        files_to_rebuild = []
        for file in request.files.getlist('filesUploaded'):
            temp_file = Files.temp_file()
            file.save(temp_file)
            files_to_rebuild.append((file.filename, file.content_type, temp_file))

        files_to_save = rebuild_files(files_to_rebuild)
        data = save_to_gofile(files_to_save)

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
    #app.run(debug=True, port=443, ssl_context=('localhost.crt', 'localhost.key'))
    app.run(debug=True, port=443, ssl_context=('gw-gofile.crt', 'gw-gofile.key'))
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

# openssl req -x509 -out gw-gofile.crt -keyout gw-gofile.key \
#   -newkey rsa:2048 -nodes -sha256 \
#   -subj '/CN=glasswall.gofile.io' -extensions EXT -config <( \
#    printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:glasswall.gofile.io\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

