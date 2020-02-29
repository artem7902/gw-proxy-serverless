import base64
import json

from gw_bot.helpers.Lambda_Helpers import log_to_elk
from osbot_aws.Dependencies import load_dependency

CONST_STACKOVERFLOW = 'stackoverflow'
CONST_GLASSWALL = 'glasswall'
CONST_GW_PROXY = 'gw-proxy'

CONST_DEFAULT_SITE = 'https://glasswall-file-drop.azurewebsites.net{}'
CONST_SITE_STACKOVERFLOW = 'https://stackoverflow.com{}'
CONST_SITE_GLASSWALL = 'https://www.glasswallsolutions.com{}'

CONST_BINARY_TYPES = [
    "application/octet-stream",
    "application/x-protobuf",
    "application/x-tar",
    "application/zip",
    "image/png",
    "image/jpeg",
    "image/jpg",
    "image/tiff",
    "image/webp",
    "image/jp2",
    'font/woff',
    'font/woff2'
]

CONST_ORIGINAL_GW_SITE = 'glasswallsolutions.com'
CONST_REPLACED_GW_SITE = 'glasswall.gw-proxy.com'

CONST_ORIGINAL_STACKOVERFLOW = 'Stack Overflow'
CONST_REPLACED_STACKOVERFLOW = '<b>[CHANGED BY THE PROXY]</b>'

CONST_SCHOOL_STEM = 'School STEM show hits the road'
CONST_REPLACED_SCHOOL_STEM = 'BAE STOP with "Glasswall Inside" available in March 2020'

CONST_PARTNERED = 'We have partnered with Royal Airforce and Royal ' \
                  'Navy to take STEM to The Belvedore Academy in Liverpool'
CONST_REPLACED_PARTNERED = 'Product available for pre-order ' \
                           'at the <a href="http://glasswall-store.com/">Glasswall Store</a>'

CONST_BAE_SYSTEMS_IMG = 'https://www.baesystems.com/en/download-en' \
                        '/multimediaimage/webImage/20200214163601/1434644561633.jpg'
CONST_REPLACED_BAE_SYSTEMS_IMG = 'https://user-images.githubusercontent.com/' \
                                 '656739/74657297-d5f10a00-5187-11ea-908a-e9f8ca79d1fa.png'

CONST_ANGER = 'Anger as historic car brand scrapped in Australia'
CONST_REPLACED_ANGER = 'BAE STOP with "Glasswall Inside" available in March 2020'

CONST_US_CAR_GIANT = 'The move comes as the US car giant ' \
                     'retreats from more markets to focus on more profitable countries.'
CONST_REPLACED_US_CAR_GIANT = 'Product available for ' \
                              'pre-order at the <a href="http://glasswall-store.com/">Glasswall Store</a>'

RESPONSE_BAD_REQUEST = 'Request body was invalid'
RESPONSE_SERVER_ERROR = 'A server error was encountered while processing the request'

class SaasBase:

    @staticmethod
    def domain_parser(cls, domain_prefix, path):
        if domain_prefix == CONST_STACKOVERFLOW:
            return CONST_SITE_STACKOVERFLOW.format(path)
        elif domain_prefix == CONST_GLASSWALL:
            return CONST_SITE_GLASSWALL.format()
        elif domain_prefix == CONST_GW_PROXY:
            return CONST_DEFAULT_SITE.format(path)
        elif domain_prefix is not None:
            return f'https://{domain_prefix.replace("_", ".")}{path}'
        return CONST_DEFAULT_SITE.format(path)

    @staticmethod
    def bad_request(cls, body):
        return {
            "statusCode": 400,
            "body": body
    }


    @staticmethod
    def server_error(cls, body):
        return {
            "statusCode": 500,
            "body": body
    }

    @staticmethod
    def ok(cls, headers, body, is_base_64):
        return {
            "isBase64Encoded": is_base_64,
            "statusCode": 200,
            "headers": headers,
            "body": body
    }

    @staticmethod
    def log_request(path, method, headers, domain_prefix, target,body):
        data = {'path': path, 'method': method, 'headers': headers, \
                'domain_prefix': domain_prefix, 'target': target, 'body': body}
        log_to_elk('proxy message', data)

    @staticmethod
    def parse_response(cls,response):
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
            response_body = response_body.replace(CONST_ORIGINAL_GW_SITE, CONST_REPLACED_GW_SITE) \
                .replace(CONST_ORIGINAL_STACKOVERFLOW, CONST_REPLACED_STACKOVERFLOW) \
                .replace(CONST_SCHOOL_STEM, CONST_REPLACED_SCHOOL_STEM) \
                .replace(CONST_PARTNERED, CONST_REPLACED_PARTNERED) \
                .replace(CONST_BAE_SYSTEMS_IMG, CONST_REPLACED_BAE_SYSTEMS_IMG) \
                .replace(CONST_ANGER, CONST_REPLACED_ANGER) \
                .replace(CONST_US_CAR_GIANT, CONST_REPLACED_US_CAR_GIANT)
        return cls.ok(response_headers, response_body, is_base_64)


class APISaasVPSClient(SaasBase):
    """Quickly and easily send http request API."""

    def __init__(self, event):
        """
        :param event: The event dictionary
        """
        self.path = event.get('path', '')
        self.method = event.get('httpMethod', '')
        self.headers = event.get('headers', {})
        self.domain_prefix = event.get('requestContext', {}).get('domainPrefix')
        self.request_headers = {'accept': self.headers.get('headers'),
                                'User-Agent': self.headers.get('User-Agent'),
                                'accept-encoding': self.headers.get('accept-encoding')}
        self.target = self.domain_parser(self.domain_prefix, self.path)
        self.body = event.get('body', {})

    def request_get(self):
        """The actual http request
        """
        try:
            load_dependency('requests')
            import requests
            self.log_request(self.path, self.method, self.headers, self.domain_prefix, self.target, , self.body)
            response = requests.get(self.target, headers=self.request_headers)
            return self.parse_response(response)
        except Exception as e:
            return SaasBase.server_error(RESPONSE_SERVER_ERROR)

    def request_post(self):
        """The actual http request
        """
        try:
            load_dependency('requests')
            import requests
            self.log_request(self.path, self.method, self.headers, self.domain_prefix, self.target, self.body)
            response = requests.post(self.target, data=json.dumps(self.body), headers=self.headers)
            return SaasBase.parse_response(response)
        except Exception as e:
            return SaasBase.bad_request(RESPONSE_BAD_REQUEST)