import base64
import json

import requests

from gw_proxy._to_sync.anish_agarwal.Proxy_Const import CONST_BINARY_TYPES, RESPONSE_SERVER_ERROR

class Http_Proxy:

    def __init__(self, body, path, headers, method, target):
        self.body            = body
        self.path            = path
        self.headers         = headers
        self.method          = method
        self.target          = target

        self.request_headers = { 'accept'         : self.headers.get('headers'        ),
                                 'User-Agent'     : self.headers.get('User-Agent'     ),
                                 'accept-encoding': self.headers.get('accept-encoding')}

    
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

    def request_post(self):
        """The POST http proxy API
        """
        try:
            response = requests.post(self.target, data=json.dumps(self.body), headers=self.headers)
            return self.parse_response(response)
        except Exception as e:
            return self.bad_request(RESPONSE_SERVER_ERROR)

    def parse_response(self, response):
        response_headers = {}
        response_body = response.content
        for key, value in response.headers.items():  # the original value of result.headers is not serializable
            if key != 'Content-Encoding':
                response_headers[key] = str(value)
        content_type = response_headers.get('Content-Type')

        if content_type in CONST_BINARY_TYPES:
            is_base_64 = True
            response_body = base64.b64encode(response_body).decode("utf-8")
        else:
            is_base_64 = False
            response_body = response.text
        return self.ok(response_headers, response_body, is_base_64)

    @staticmethod
    def bad_request(body):
        return { "statusCode": 400 ,
                 "body"     : f'{body}' }

    @staticmethod
    def server_error(body):
        return { "statusCode": 500 ,
                 "body"      : f'{body}' }

    @staticmethod
    def ok(headers, body, is_base_64):
        return { "isBase64Encoded": is_base_64,
                 "statusCode"     : 200       ,
                 "headers"        : headers   ,
                 "body"           : body      }