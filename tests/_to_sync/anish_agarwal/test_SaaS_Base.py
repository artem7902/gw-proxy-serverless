from unittest import TestCase

from gw_proxy._to_sync.anish_agarwal.Saas_Base import Saas_Base


class test_SaaS_Base(TestCase):

    def test_domain_parser(self):
        self.assertEqual(Saas_Base().domain_parser(None, 'stackoverflow', '/AAAAA'), 'https://stackoverflow.com/AAAAA'                    )
        self.assertEqual(Saas_Base().domain_parser(None, 'glasswall'    , '/AAAAA'), 'https://www.glasswallsolutions.com/AAAAA'           )
        self.assertEqual(Saas_Base().domain_parser(None, 'gw-proxy'     , '/AAAAA'), 'https://glasswall-file-drop.azurewebsites.net/AAAAA')
        self.assertEqual(Saas_Base().domain_parser(None, 'aaaa'         , '/AAAAA'), 'https://aaaa/AAAAA'                                 )
        self.assertEqual(Saas_Base().domain_parser(None, 'aaaa'         , '/A?a=b'), 'https://aaaa/A?a=b'                                 )
        self.assertEqual(Saas_Base().domain_parser(None, 'aaaa'         , '/A#a=b'), 'https://aaaa/A#a=b'                                 )
        self.assertEqual(Saas_Base().domain_parser(None, 'aaaa'         , '/A?a#b'), 'https://aaaa/A?a#b'                                 )
        self.assertEqual(Saas_Base().domain_parser(None, None           , '/AAAAA'), 'https://glasswall-file-drop.azurewebsites.net/AAAAA')

        ## todo: improve handling of these edge cases:

        self.assertEqual(Saas_Base().domain_parser(None, 'aaaa'         , None    ), 'https://aaaaNone'                                   ) # None ends in path
        self.assertEqual(Saas_Base().domain_parser(None, 'aaaa'         , 'BBB'   ), 'https://aaaaBBB'                                    ) # path breaks url
        self.assertEqual(Saas_Base().domain_parser('--', 'aaaa'         , None    ), 'https://aaaaNone'                                   ) # cls value is not used

        ## with security implications

        self.assertEqual(Saas_Base().domain_parser('--', 'abc.com/aaa/' , None    ), 'https://abc.com/aaa/None'                           ) # domain adds path
        self.assertEqual(Saas_Base().domain_parser('--', '../aaa/'      , None    ), 'https://../aaa/None'                                ) # invalid domain
        self.assertEqual(Saas_Base().domain_parser('--', 'a:b@cc'       , None    ), 'https://a:b@ccNone'                                 ) # domain contain pwd
        self.assertEqual(Saas_Base().domain_parser('--', 'aaa'          , '/../aa'), 'https://aaa/../aa'                                  ) # path transversal



        #try:
        #    print(Saas_Base().domain_parser(None, 'glasswall',None))
        #except Exception as error:
        #    assert error.args[0] =='Replacement index 0 out of range for positional args tuple'


