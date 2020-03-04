from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    print('*********in Socket')
    while not ws.closed:
        message = ws.receive()
        print(f'**** message : {message} ')
        ws.send(message)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 12345), app, handler_class=WebSocketHandler)
    server.serve_forever()