from unittest import TestCase

from gw_proxy.api.Lambda_Event import Lambda_Event


class test_Lambda_Event(TestCase):

    def setUp(self) -> None:
        self.params       = {}
        self.lambda_event = Lambda_Event(self.params)

    # todo: improve test
    def test_ctor(self):
        self.assertEqual(self.lambda_event.lambda_data    , {'body': {}, 'path': '', 'method': '', 'domain_prefix': None, 'headers': {}})
        self.assertEqual(self.lambda_event.http_proxy.body, {})

    def test_domain_parser(self):
        domain_parser = self.lambda_event.domain_parser
        self.assertEqual(domain_parser('stackoverflow', '/AAAAA'), 'https://stackoverflow.com/AAAAA'                    )
        self.assertEqual(domain_parser('glasswall'    , '/AA/AA'), 'https://www.glasswallsolutions.com/AA/AA'           )
        self.assertEqual(domain_parser('gw-proxy'     , '/A/A/A'), 'https://glasswall-file-drop.azurewebsites.net/A/A/A')
        self.assertEqual(domain_parser('aaaa'         , '/AAAAA'), 'https://aaaa/AAAAA'                                 )
        self.assertEqual(domain_parser('aaaa'         , '/A?a=b'), 'https://aaaa/A?a=b'                                 )
        self.assertEqual(domain_parser('aaaa'         , '/A#a=b'), 'https://aaaa/A#a=b'                                 )
        self.assertEqual(domain_parser('aaaa'         , '/A?a#b'), 'https://aaaa/A?a#b'                                 )
        self.assertEqual(domain_parser('aaaa'         , 'BBB/cc'), 'https://aaaa/BBB/cc'                                )

        ## handle null values
        self.assertEqual(domain_parser( None          , '/AAAAA'), 'https://glasswall-file-drop.azurewebsites.net/AAAAA')
        self.assertEqual(domain_parser('aaaa'         , None    ), 'https://aaaa'                                       )

        ## with security implications
        self.assertEqual(domain_parser('abc.com/aaa/' , None    ), 'https://abc.com/aaa/'                               ) # domain adds path
        self.assertEqual(domain_parser('../aaa/'      , None    ), 'https://../aaa/'                                    ) # invalid domain
        self.assertEqual(domain_parser('a:b@cc'       , None    ), 'https://a:b@cc'                                     ) # domain contain pwd
        self.assertEqual(domain_parser('aaa'          , '/../aa'), 'https://aaa/../aa'                                  ) # path transversal

    # todo: move to integration tests

    def test_get_response__postman_echo(self):
        params       = {'httpMethod' : 'GET' , 'path': 'get?foo1=bar1&foo2=bar2', 'domain_prefix': 'postman-echo.com'}
        lambda_event = Lambda_Event(params)
        result       = lambda_event.get_response()
        print(lambda_event.http_proxy.target)