import json

import requests

from gw_proxy._to_sync.anish_agarwal.Proxy_Const import RESPONSE_SERVER_ERROR
from gw_proxy._to_sync.anish_agarwal.Saas_Base   import Saas_Base


class API_SaaS_VPS_Client(Saas_Base):
    """Quickly and easily send http request API."""

    def __init__(self, event):
        """
        :param event: The event dictionary
        """
        self.body            = event.get('body'          , {}                         )
        self.path            = event.get('path'          , ''                         )
        self.headers         = event.get('headers'       , {}                         )
        self.method          = event.get('httpMethod'    , ''                         )
        self.domain_prefix   = event.get('requestContext', {}).get('domainPrefix'     )
        self.target          = self.domain_parser ( self.domain_prefix, self.path      )
        self.request_headers = { 'accept'         : self.headers.get('accept'        ),
                                 'User-Agent'     : self.headers.get('User-Agent'     ),
                                 'accept-encoding': self.headers.get('accept-encoding')}

    def request_get(self):
        """The GET http proxy API
        """
        try:
            self.log_request(self.path, self.method, self.headers, self.domain_prefix, self.target, self.body)
            response = requests.get(self.target, headers=self.request_headers)
            return self.parse_response(response)
        except Exception as e:
            return Saas_Base.server_error(RESPONSE_SERVER_ERROR)

    def request_post(self):
        """The POST http proxy API
        """
        try:
            self.log_request(self.path, self.method, self.headers, self.domain_prefix, self.target, self.body)
            response = requests.post(self.target, data=json.dumps(self.body), headers=self.headers)
            return Saas_Base.parse_response(response)
        except Exception as e:
            return Saas_Base.bad_request(RESPONSE_SERVER_ERROR)