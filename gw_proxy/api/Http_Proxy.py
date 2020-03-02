import base64
import json

import requests
import urllib3

class Http_Proxy:

    def __init__(self, target=None, method='GET', body='', headers={}):
        self.body            = body
        self.headers         = headers
        self.method          = method
        self.target          = target
        self.skip_headers    = ['host', 'accept-encoding','accept']
        self.verify_ssl      = True             # move to site specific settings
        
        #self.verify_ssl      = False            # for now disable this since it was causing probs on some sites (like gofile.io)
        #urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def make_request(self):
        if self.method == 'GET':
            return self.request_get()
        elif self.method == 'POST':
            return self.request_post()
        elif self.method == 'OPTIONS':
            return self.request_options()
        else:
            return {'error': f'unsupported method: {self.method}'}

    # def is_binary_content_type(self, response):
    #     return response.headers.get('Content-Type') in BINARY_CONTENT_TYPES

    # def get_response_body(self, response):
    #     if self.is_binary_content_type(response):
    #         response_body = base64.b64encode(response.content).decode('utf-8')
    #     else:
    #         response_body = response.text
    #     return response_body

    def parse_response(self,response):
        response_headers = {}
        for key, value in response.headers.items():  # the original value of result.headers is not serializable
            if key != 'Content-Encoding':
                response_headers[key] = str(value)

        # todo: move to lambda specific code
        # response_body = response.content
        #content_type = response_headers.get('Content-Type')

        #if content_type in CONST_BINARY_TYPES:
        #    is_base_64 = True
        #    response_body = base64.b64encode(response_body).decode("utf-8")
        #else:
        #    is_base_64 = False
        #    response_body = response.content
        is_base_64 = False
        response_body = response.content

        return self.ok(response_headers, response_body, is_base_64)

    def request_headers(self):
        #print('****** request headers*****')
        result = {}
        for key, value in self.headers.items():
            if key.lower() not in self.skip_headers:
                result[key.lower()] = value
                #print(f'{key} = {value}')
        return result

    def request_get(self):
        """The GET http proxy API
        """
        try:
            response = requests.get(self.target, headers=self.request_headers(), verify=self.verify_ssl)
            return self.parse_response(response)
        except Exception as error:
            return self.bad_request(error)


    def request_options(self):
        """The GET http proxy API
        """
        try:
            response = requests.options(self.target, headers=self.request_headers(), verify=self.verify_ssl)
            return self.parse_response(response)
        except Exception as error:
            return self.bad_request(error)

    # bug: this is only supporting json payloads
    def request_post(self):
        """The POST http proxy API
        """
        try:

            #if self.headers.get('Content-Type') =='application/x-www-form-urlencoded' and type(self.body) is bytes:
            #    self.body = self.body.decode()

            print()
            print('****** POST DATA*****')
            print(self.request_headers().get('content-length') , len(self.body))
            print(self.body)
            print('###### POST DATA ####')
            response = requests.post(self.target, data=self.body, headers=self.request_headers(), verify=self.verify_ssl)
            return self.parse_response(response)
        except Exception as error:
            return self.bad_request(error)

    @staticmethod
    def bad_request(body):                  # todo: move to helper class
        if type(body) is not bytes:
            body = str(body).encode()
        return { "statusCode": 400 ,
                 "headers"  : {}   ,        # todo: also return headers
                 "body"     : body }

    @staticmethod
    def server_error(body):                 # todo: move to helper class
        return { "statusCode": 500  ,
                 "headers"   : {}   ,       # todo: also return headers
                 "body"      : body }

    @staticmethod
    def ok(headers, body, is_base_64):
        return { "isBase64Encoded": is_base_64,
                 "statusCode"     : 200       ,
                 "headers"        : headers   ,
                 "body"           : body      }