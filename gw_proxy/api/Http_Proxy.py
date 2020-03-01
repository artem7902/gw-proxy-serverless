class Http_Proxy:

    def __init__(self):
        self.lambda_event = None

    def handle_lambda_event(self, event):
        """
        :param event: data received from Lambda functions
        """
        headers = event.get('headers',{})
        self.lambda_event = {   'body'            : event.get('body'          , {}                         ),
                                'path'            : event.get('path'          , ''                         ),
                                'method'          : event.get('httpMethod'    , ''                         ),
                                'domain_prefix'   : event.get('requestContext', {}).get('domainPrefix'     ),
                                'headers'         : headers                                                 ,
                                'request_headers' : { 'accept'         : headers.get('accept'              ),
                                                      'User-Agent'     : headers.get('User-Agent'          ),
                                                      'accept-encoding': headers.get('accept-encoding'    )}}
