from urllib.parse import urlparse, ParseResult, urlunparse

from gw_proxy._to_sync.anish_agarwal.Proxy_Const import CONST_STACKOVERFLOW, CONST_GLASSWALL, CONST_GW_PROXY, \
                                                        CONST_SITE_STACKOVERFLOW, CONST_SITE_GLASSWALL, CONST_DEFAULT_SITE
from gw_proxy.api.Http_Proxy import Http_Proxy


class Lambda_Event:

    def __init__(self, event):
        """
        :param event: data received from Lambda functions
        """
        self.lambda_data = { 'body'            : event.get('body'          , {}                         ),
                             'path'            : event.get('path'          , ''                         ),
                             'method'          : event.get('httpMethod'    , ''                         ),
                             'domain_prefix'   : event.get('requestContext', {}).get('domainPrefix'     ),
                             'headers'         : event.get('headers'       , {}                         )}

        self.target = self.domain_parser(event.get('domain_prefix'), self.lambda_data.get('path'))
        self.http_proxy = Http_Proxy(body          = self.lambda_data.get('body'         ),
                                     path          = self.lambda_data.get('path'         ),
                                     headers       = self.lambda_data.get('headers'      ),
                                     method        = self.lambda_data.get('method'       ),
                                     #domain_prefix = self.lambda_data.get('domain_prefix'),
                                     target        = self.target)

    def domain_parser(self, domain_prefix, path=''):
        if   domain_prefix  == CONST_STACKOVERFLOW  : target_domain = CONST_SITE_STACKOVERFLOW
        elif domain_prefix  == CONST_GLASSWALL      : target_domain = CONST_SITE_GLASSWALL
        elif domain_prefix  == CONST_GW_PROXY       : target_domain = CONST_DEFAULT_SITE
        elif domain_prefix is not None              : target_domain = domain_prefix.replace("_", ".")
        else                                        : target_domain = CONST_DEFAULT_SITE

        parsed_path = urlparse(path or '')
        url = urlunparse(ParseResult(scheme='https'           , netloc=target_domain    , path     =parsed_path.path,
                                     params=parsed_path.params, query =parsed_path.query, fragment=parsed_path.fragment))
        return url

    def get_response(self):
        return self.http_proxy.make_request()