from unittest import TestCase,mock
from http import HTTPStatus
from gw_proxy._to_sync.anish_agarwal.API_SaaS_VPS_Client import API_SaaS_VPS_Client

class test_Rest_API_SaaS_VPs(TestCase):

    @mock.patch('requests.get')
    def test_proxy_for_brotli_encoded_sites(self, mockget):
        # Mock response
        headers = {
            "Date"                                      :   "Sun, 01 Mar 2020 11:22:05 GMT",
            "Expires"                                   :   "-1",
            "Cache-Control"                             :   "private, max-age=0",
            "Content-Type"                              :   "text/html; charset=UTF-8",
            "Strict-Transport-Security"                 :   "max-age=31536000",
            "Accept-CH"                                 :   "DPR",
            "Accept-CH-Lifetime"                        :   "2592000",
            "P3P"                                       :   "CP=\"This is not a P3P policy! See g.co/p3phelp for more info.\"",
            "Content-Encoding"                          :   "br",
            "Content-Length"                            :   "65251",
            "X-XSS-Protection"                          :   "0",
            "X-Frame-Options"                           :   "SAMEORIGIN",
            "Set-Cookie"                                :  "1P_JAR=2020-03-01-11; expires=Tue, 31-Mar-2020 11:22:06 GMT; path=/; domain=.google.com; Secure; SameSite=none, NID=199=UsFpcFnQ21COTv9q0Scd3ZUVZBDiHmy0Wts3igOy3v8iHYmlDnv7PbiF_JyecNwwWTUlzjNfp6-b50Igyf0c9CbkirOK9azAy6HWh1TLzCTSUJHbw6_tfZexErwcYNu1F9fXeIOUDJWUrC21DVSJsWg1cCpPrc9d71IbO-9X1dE; expires=Mon, 31-Aug-2020 11:22:05 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=none",
            "Alt-Svc"                                   :  "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000"
        }
        params                                          =  {'headers.return_value': headers}
        response                                        =  mock.Mock(**params)
        response.headers                                =  headers
        response.content                                =  b'some-test-bytes-string'
        mockget.return_value                            =  response
        # The request
        body                                            =  {}
        path                                            =  '/'
        method                                          =  'GET'
        domain_prefix                                   =  'https://google.com'
        self.request_headers = {
            'accept'                                    :  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent'                                :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'accept-encoding'                           :  'gzip,deflate,br'
        }
        requestContext = {
            "resourcePath"                              :  "/",
            "httpMethod"                                :  "GET",
            "path"                                      :  "/",
            "protocol"                                  :  "HTTP/1.1",
            "domainPrefix"                              :  domain_prefix,
            "domainName"                                :  domain_prefix
        }
        event = {
            "body"                                      :  body,
            "path"                                      :  path,
            "headers"                                   :  headers,
            "httpMethod"                                :  method,
            "requestContext"                            :  requestContext
        }
        api_saas_vps_client = API_SaaS_VPS_Client(event)
        result                                          =  api_saas_vps_client.request_get()
        assert result['isBase64Encoded']                == True
        assert result['headers']['Content-Encoding']    == 'br'
        assert result['statusCode']                     == HTTPStatus.OK.value
        assert result['body']                           == 'c29tZS10ZXN0LWJ5dGVzLXN0cmluZw=='


    @mock.patch('requests.get')
    def test_proxy_for_gzip_encoded_sites(self, mockget):
        # Mock response
        headers = {
            "Date"                                      :   "Sun, 01 Mar 2020 11:22:05 GMT",
            "Expires"                                   :   "-1",
            "Cache-Control"                             :   "private, max-age=0",
            "Content-Type"                              :   "text/html; charset=UTF-8",
            "Content-Encoding"                          :   "gzip",
            "Content-Length"                            :   "65251",
            "X-XSS-Protection"                          :   "0",
            "X-Frame-Options"                           :   "SAMEORIGIN",
            "Set-Cookie"                                :  "1P_JAR=2020-03-01-11; expires=Tue, 31-Mar-2020 11:22:06 GMT; path=/; domain=.google.com; Secure; SameSite=none, NID=199=UsFpcFnQ21COTv9q0Scd3ZUVZBDiHmy0Wts3igOy3v8iHYmlDnv7PbiF_JyecNwwWTUlzjNfp6-b50Igyf0c9CbkirOK9azAy6HWh1TLzCTSUJHbw6_tfZexErwcYNu1F9fXeIOUDJWUrC21DVSJsWg1cCpPrc9d71IbO-9X1dE; expires=Mon, 31-Aug-2020 11:22:05 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=none",
            "Alt-Svc"                                   :  "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000"
        }
        params                                          =  {'headers.return_value': headers}
        response                                        =  mock.Mock(**params)
        response.headers                                =  headers
        response.content                                =  b'some-test-bytes-string'
        mockget.return_value                            =  response
        # The request
        body                                            =  {}
        path                                            =  '/'
        method                                          =  'GET'
        domain_prefix                                   =  'https://google.com'
        self.request_headers = {
            'accept'                                    :  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent'                                :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'accept-encoding'                           :  'gzip,deflate,br'
        }
        requestContext = {
            "resourcePath"                              :  "/",
            "httpMethod"                                :  "GET",
            "path"                                      :  "/",
            "protocol"                                  :  "HTTP/1.1",
            "domainPrefix"                              :  domain_prefix,
            "domainName"                                :  domain_prefix
        }
        event = {
            "body"                                      :  body,
            "path"                                      :  path,
            "headers"                                   :  headers,
            "httpMethod"                                :  method,
            "requestContext"                            :  requestContext
        }
        api_saas_vps_client = API_SaaS_VPS_Client(event)
        result                                          =  api_saas_vps_client.request_get()
        assert result['isBase64Encoded']                == True
        assert 'Content-Encoding' not in                   result['headers']
        assert result['statusCode']                     == HTTPStatus.OK.value
        assert result['body']                           == 'c29tZS10ZXN0LWJ5dGVzLXN0cmluZw=='

    @mock.patch('requests.get')
    def test_proxy_for_unencoded_sites(self, mockget):
        # Mock response
        headers = {
            "Date"                                      :   "Sun, 01 Mar 2020 11:22:05 GMT",
            "Expires"                                   :   "-1",
            "Cache-Control"                             :   "private, max-age=0",
            "Content-Type"                              :   "text/html",
            "Content-Length"                            :   "65251",
            "X-XSS-Protection"                          :   "0",
            "X-Frame-Options"                           :   "SAMEORIGIN",
            "Set-Cookie"                                :  "1P_JAR=2020-03-01-11; expires=Tue, 31-Mar-2020 11:22:06 GMT; path=/; domain=.google.com; Secure; SameSite=none, NID=199=UsFpcFnQ21COTv9q0Scd3ZUVZBDiHmy0Wts3igOy3v8iHYmlDnv7PbiF_JyecNwwWTUlzjNfp6-b50Igyf0c9CbkirOK9azAy6HWh1TLzCTSUJHbw6_tfZexErwcYNu1F9fXeIOUDJWUrC21DVSJsWg1cCpPrc9d71IbO-9X1dE; expires=Mon, 31-Aug-2020 11:22:05 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=none",
            "Alt-Svc"                                   :  "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000"
        }
        params                                          =  {'headers.return_value': headers}
        response                                        =  mock.Mock(**params)
        response.headers                                =  headers
        response.text                                   =  'some-test-bytes-string'
        mockget.return_value                            =  response
        # The request
        body                                            =  {}
        path                                            =  '/'
        method                                          =  'GET'
        domain_prefix                                   =  'https://google.com'
        self.request_headers = {
            'accept'                                    :  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent'                                :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'accept-encoding'                           :  'gzip,deflate,br'
        }
        requestContext = {
            "resourcePath"                              :  "/",
            "httpMethod"                                :  "GET",
            "path"                                      :  "/",
            "protocol"                                  :  "HTTP/1.1",
            "domainPrefix"                              :  domain_prefix,
            "domainName"                                :  domain_prefix
        }
        event = {
            "body"                                      :  body,
            "path"                                      :  path,
            "headers"                                   :  headers,
            "httpMethod"                                :  method,
            "requestContext"                            :  requestContext
        }
        api_saas_vps_client = API_SaaS_VPS_Client(event)
        result                                          =  api_saas_vps_client.request_get()
        assert result['isBase64Encoded']                == False
        assert 'Content-Encoding' not in                   result['headers']
        assert result['statusCode']                     == HTTPStatus.OK.value
        assert result['body']                           == 'some-test-bytes-string'