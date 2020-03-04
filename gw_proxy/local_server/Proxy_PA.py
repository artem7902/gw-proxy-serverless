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

SITE_NAME = 'https://www.paconsulting.com/'


def apply_transformations(response_body, response_headers):
    #target_files = ['application/javascript', 'text/html; charset=utf-8', 'text/html']
    target_files = ['text/html; charset=utf-8']
    if response_headers.get('Content-Type', '').lower() in target_files:
        new_body = response_body.decode()
        new_body = new_body.replace('/Static/images/svgs/logo.svg', 'https://user-images.githubusercontent.com/656739/75869539-9c640400-5e01-11ea-8b47-03effdd766e5.png')
        new_body = new_body.replace('Request for proposal</h1>', 'Request for proposal<h1><h3>(Secured by Glasswall)</h3><hr>')
        new_body = new_body.replace('The number of files you have uploaded will be displayed next to the attachments button.', '<br/><p>All files uploaded will be rebuild using the Glasswall engine.</p>')
        jquery_fixes ="$('.header-logo img').width('160px')"
        new_body = new_body.replace('</body>',f'<script>{jquery_fixes}</script></body>')
        return new_body.encode()

    return response_body
        
@app.route('/')
@app.route('/<path:path>',methods=['GET','POST',"PUT","DELETE"])
def proxy(path=''):
    global SITE_NAME
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection','host']
    try:
        target= f'{SITE_NAME}{path}'
        if request.method=='GET':
            response = Http_Proxy(target=target,method='GET',headers=request.headers).make_request()
            #transformed_body = response.get('body').decode('utf-8').encode('utf-8')
            transformed_body = apply_transformations(response.get('body'), response.get('headers'))
            return Response(transformed_body, response.get('statusCode'),response.get('headers'))


        elif request.method=='POST':
            response = Http_Proxy(target=target, method='POST', headers=request.headers,body=request.get_data()).make_request()
            return Response(response.get('body'), response.get('statusCode'), response.get('headers'))

    except Exception as error:
        return f'{error}'

if __name__ == '__main__':
    app.run(debug = True,port=80)
    #app.run(debug=True, port=1443, ssl_context=('localhost.crt', 'localhost.key'))