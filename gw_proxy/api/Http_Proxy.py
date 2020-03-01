import base64
import json

import requests

from gw_proxy._to_sync.andrii_tykhonov.api.proxy import BINARY_CONTENT_TYPES
from gw_proxy._to_sync.anish_agarwal.Proxy_Const import CONST_BINARY_TYPES, RESPONSE_SERVER_ERROR

class Http_Proxy:

    def __init__(self, target, method='GET', body='', headers={}):
        self.body            = body
        self.headers         = headers
        self.method          = method
        self.target          = target

        self.request_headers = { #'accept'         : self.headers.get('accept'        ),
                                 'User-Agent'     : self.headers.get('User-Agent'     ),
                                 'accept-encoding': self.headers.get('accept-encoding')}

    def make_request(self):
        if self.method == 'GET':
            return self.request_get()
        elif self.method == 'POST':
            return self.request_post()
        else:
            return {'error': f'unsupported method: {self.method}'}

    def is_binary_content_type(self, response):
        return response.headers.get('Content-Type') in BINARY_CONTENT_TYPES

    def get_response_body(self, response):
        if self.is_binary_content_type(response):
            response_body = base64.b64encode(response.content).decode('utf-8')
        else:
            response_body = response.text
        return response_body

    def parse_response(self,response):
        response_headers = {}

        response_body = response.content
        for key, value in response.headers.items():  # the original value of result.headers is not serializable
            if key != 'Content-Encoding':
                response_headers[key] = str(value)
        content_type = response_headers.get('Content-Type')

        #if content_type in CONST_BINARY_TYPES:
        #    is_base_64 = True
        #    response_body = base64.b64encode(response_body).decode("utf-8")
        #else:
        #    is_base_64 = False
        #    response_body = response.content
        is_base_64 = False
        response_body = response.content
        return self.ok(response_headers, response_body, is_base_64)

    def request_get(self):
        """The GET http proxy API
        """
        try:
            #self.log_request(self.path, self.method, self.headers, self.domain_prefix, self.target, self.body)
            response = requests.get(self.target, headers=self.request_headers)
            return self.parse_response(response)
        except Exception as e:
            return None
            #return Saas_Base.server_error(RESPONSE_SERVER_ERROR)

    # bug: this is only supporting json payloads
    def request_post(self):
        """The POST http proxy API
        """
        try:
            response = requests.post(self.target, data=json.dumps(self.body), headers=self.headers)
            return self.parse_response(response)
        except Exception as e:
            return self.bad_request(RESPONSE_SERVER_ERROR)

    @staticmethod
    def bad_request(body):                  # todo: move to helper class
        return { "statusCode": 400 ,
                 "body"     : body }

    @staticmethod
    def server_error(body):                 # todo: move to helper class
        return { "statusCode": 500 ,
                 "body"      : body }

    @staticmethod
    def ok(headers, body, is_base_64):
        return { "isBase64Encoded": is_base_64,
                 "statusCode"     : 200       ,
                 "headers"        : headers   ,
                 "body"           : body      }