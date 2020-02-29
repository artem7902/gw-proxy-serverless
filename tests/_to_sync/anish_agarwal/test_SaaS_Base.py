from unittest import TestCase

from gw_proxy._to_sync.anish_agarwal.Saas_Base import Saas_Base


class test_SaaS_Base(TestCase):
    def setUp(self):
        self.saas_base = Saas_Base()

    def test_domain_parser(self):
        domain_parser = self.saas_base.domain_parser
        self.assertEqual(domain_parser('stackoverflow', '/AAAAA'), 'https://stackoverflow.com/AAAAA'                    )
        self.assertEqual(domain_parser('glasswall'    , '/AAAAA'), 'https://www.glasswallsolutions.com/AAAAA'           )
        self.assertEqual(domain_parser('gw-proxy'     , '/AAAAA'), 'https://glasswall-file-drop.azurewebsites.net/AAAAA')
        self.assertEqual(domain_parser('aaaa'         , '/AAAAA'), 'https://aaaa/AAAAA'                                 )
        self.assertEqual(domain_parser('aaaa'         , '/A?a=b'), 'https://aaaa/A?a=b'                                 )
        self.assertEqual(domain_parser('aaaa'         , '/A#a=b'), 'https://aaaa/A#a=b'                                 )
        self.assertEqual(domain_parser('aaaa'         , '/A?a#b'), 'https://aaaa/A?a#b'                                 )
        self.assertEqual(domain_parser('aaaa'         , 'BBB'   ), 'https://aaaa/BBB'                                   )

        ## handle null values
        self.assertEqual(domain_parser(None           , '/AAAAA'), 'https://glasswall-file-drop.azurewebsites.net/AAAAA')
        self.assertEqual(domain_parser('aaaa'         , None    ), 'https://aaaa'                                       )
        self.assertEqual(domain_parser('aaaa'         , None    ), 'https://aaaa'                                       ) # cls value is not used

        ## with security implications

        self.assertEqual(domain_parser('abc.com/aaa/' , None    ), 'https://abc.com/aaa/'                               ) # domain adds path
        self.assertEqual(domain_parser('../aaa/'      , None    ), 'https://../aaa/'                                    ) # invalid domain
        self.assertEqual(domain_parser('a:b@cc'       , None    ), 'https://a:b@cc'                                     ) # domain contain pwd
        self.assertEqual(domain_parser('aaa'          , '/../aa'), 'https://aaa/../aa'                                  ) # path transversal

    def test_bad_request(self):
        self.assertEqual(self.saas_base.bad_request('el-body'),  {'statusCode': 400, 'body': 'el-body'})

    def test_server_error(self):
        self.assertEqual(self.saas_base.server_error('el-body'),  {'statusCode': 500, 'body': 'el-body'})

    def test_server_ok(self):
        is_base_64 = False
        headers    = {'an': 'header'}
        body       = 'el-body'

        self.assertEqual(self.saas_base.ok(headers, body,is_base_64),  {'isBase64Encoded': is_base_64, 'statusCode': 200, 'headers':headers, 'body': 'el-body'})


