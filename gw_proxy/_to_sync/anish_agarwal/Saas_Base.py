import base64
import json
import requests


class Saas_Base:

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


