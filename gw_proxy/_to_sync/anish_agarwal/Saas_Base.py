import base64
from urllib.parse import urlunparse, ParseResult, urlparse

from gw_proxy._to_sync.anish_agarwal import Proxy_Const
from gw_proxy._to_sync.anish_agarwal.Proxy_Const import CONST_BINARY_TYPES


class Saas_Base:

    @staticmethod
    def domain_parser(domain_prefix, path):
        if   domain_prefix  == Proxy_Const.CONST_STACKOVERFLOW  : target_domain = Proxy_Const.CONST_SITE_STACKOVERFLOW
        elif domain_prefix  == Proxy_Const.CONST_GLASSWALL      : target_domain = Proxy_Const.CONST_SITE_GLASSWALL
        elif domain_prefix  == Proxy_Const.CONST_GW_PROXY       : target_domain = Proxy_Const.CONST_DEFAULT_SITE
        elif domain_prefix is not None                          : target_domain = domain_prefix.replace("_", ".")
        else                                                    : target_domain = Proxy_Const.CONST_DEFAULT_SITE

        parsed_path = urlparse(path or '')
        url = urlunparse(ParseResult(scheme='https'           , netloc=target_domain    , path     =parsed_path.path,
                                     params=parsed_path.params, query =parsed_path.query, fragment=parsed_path.fragment))
        return url

    @staticmethod
    def bad_request(body):
        return { "statusCode": 400 ,
                 "body"     : f'{body}' }

    @staticmethod
    def server_error(body):
        return { "statusCode": 500 ,
                "body"       : f'{body}' }

    @staticmethod
    def ok(headers, body, is_base_64):
        return { "isBase64Encoded": is_base_64,
                 "statusCode"     : 200       ,
                 "headers"        : headers   ,
                 "body"           : body      }

    @staticmethod
    def log_request(path, method, headers, domain_prefix, target,body):
        data = {'path': path, 'method': method, 'headers': headers, 
                'domain_prefix': domain_prefix, 'target': target, 'body': body}
        # log_to_elk('proxy message', data)         # todo: figure out best way to do this

    def parse_response(self,response):
        response_headers = {}
        response_body = response.content
        for key, value in response.headers.items():  # the original value of result.headers is not serializable
            if key == 'Content-Encoding':
                if str(value) == Proxy_Const.CONST_HEADER_BROTLI_ENCODING:
                    response_headers[key] = str(value)
            else:
                response_headers[key] = str(value)
        content_type = response_headers.get('Content-Type')

        if content_type in CONST_BINARY_TYPES:
            is_base_64 = True
            response_body = base64.b64encode(response_body).decode("utf-8")
        else:
            is_base_64 = False
            response_body = response.text
            # response_body = response_body.replace(CONST_ORIGINAL_GW_SITE, CONST_REPLACED_GW_SITE) \
            #     .replace(CONST_ORIGINAL_STACKOVERFLOW, CONST_REPLACED_STACKOVERFLOW) \
            #     .replace(CONST_SCHOOL_STEM, CONST_REPLACED_SCHOOL_STEM) \
            #     .replace(CONST_PARTNERED, CONST_REPLACED_PARTNERED) \
            #     .replace(CONST_BAE_SYSTEMS_IMG, CONST_REPLACED_BAE_SYSTEMS_IMG) \
            #     .replace(CONST_ANGER, CONST_REPLACED_ANGER) \
            #     .replace(CONST_US_CAR_GIANT, CONST_REPLACED_US_CAR_GIANT)
        return self.ok(response_headers, response_body, is_base_64)


