import requests

class Http_Proxy:

    def __init__(self, target=None, method='GET', body='', headers={}):
        self.body                  = body
        self.headers               = headers
        self.method                = method
        self.target                = target
        self.skip_request_headers  = ['host', 'accept-encoding', 'accept', 'origin','referer']
        self.skip_response_headers = ['content-encoding', 'transfer-encoding', 'content-length']
        self.verify_ssl            = True             # move to site specific settings
        
        #self.verify_ssl      = False            # for now disable this since it was causing probs on some sites (like gofile.io)
        #urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # todo: refactor to use solution like the one at Response_Handler
    def apply_transformations(self, response_body, response_headers):
        if response_headers.get('Content-Type','').lower() == 'text/html; charset=utf-8':  #todo: change headers to lower case

            content = response_body.decode()

            ###### transformation 1 : replace server urls
            local_server = 'https://demo-local.pydio.com'
            target_server = 'https://demo.pydio.com'
            content = content.replace(target_server, local_server)
            content = content.replace('demo.pydio.com', 'demo-local.pydio.com')

            target_server = 'https://glasswallsolutions.com'
            content = content.replace(target_server, local_server)

            local_server = 'http://127.0.0.1:12345/'
            target_server = 'https://send.firefox.com/'

            content = content.replace(target_server, local_server)

            return content.encode()

            #print(response_headers)
        return response_body

    def make_request(self):
        if self.method == 'GET':
            return self.request_get()
        elif self.method == 'POST':
            return self.request_post()
        elif self.method == 'PUT':
            return self.request_put()
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

    def response_headers(self, response):
        response_headers = {}
        for key, value in response.headers.items():  # the original value of result.headers is not serializable
            if key.lower() not in self.skip_response_headers:
                response_headers[key] = value
        return response_headers

    def parse_response(self,response):
        response_body    = response.content
        response_headers = self.response_headers(response)
        transformed_body = self.apply_transformations(response_body, response_headers)
        return self.ok(response_headers, transformed_body)

        # todo: move to lambda specific code
        # is_base_64 = False    # lanbda is the one that needs this
        # response_body = response.content
        #content_type = response_headers.get('Content-Type')

        #if content_type in CONST_BINARY_TYPES:
        #    is_base_64 = True
        #    response_body = base64.b64encode(response_body).decode("utf-8")
        #else:
        #    is_base_64 = False
        #    response_body = response.content

    def request_headers(self):
        #print(f'****** request headers (Start): {self.target}')
        result = {}
        for key, value in self.headers.items():
            if key.lower() not in self.skip_request_headers:
                result[key] = value
                #result[key] = value.replace('https://demo-local.pydio.com','https://demo.pydio.com')
                #result[key] = result[key].replace('demo-local.pydio.com', 'demo.pydio.com')
                #result[key] = result[key].replace('http://demo.pydio.com','https://demo.pydio.com')
                #print(f'{key} = {result[key]}')
        #print(f'****** request headers (End):')
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
        """The OPTIONS http proxy API
        """
        try:
            response = requests.options(self.target, headers=self.request_headers(), verify=self.verify_ssl)
            return self.parse_response(response)
        except Exception as error:
            return self.bad_request(error)

    # bug: this is not working for multiple sites
    def request_post(self):
        """The POST http proxy API
        """
        try:
            #if self.headers.get('Content-Type') =='application/x-www-form-urlencoded' and type(self.body) is bytes:
            #    self.body = self.body.decode()
            response = requests.post(self.target, data=self.body, headers=self.request_headers(), verify=self.verify_ssl)
            return self.parse_response(response)
        except Exception as error:
            return self.bad_request(error)

    def request_put(self):
        """The POST http proxy API
        """
        try:
            response = requests.put(self.target, data=self.body, headers=self.request_headers(), verify=self.verify_ssl)
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
    def ok(headers, body):
        return { #"isBase64Encoded": is_base_64,
                 "statusCode"     : 200       ,
                 "headers"        : headers   ,
                 "body"           : body      }