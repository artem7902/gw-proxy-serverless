from unittest import TestCase

from gw_proxy._to_sync.anish_agarwal.Saas_Base import Saas_Base


class test_SaaS_Base(TestCase):

    def test_domain_parser_bug(self):
        try:
            print(Saas_Base().domain_parser(None, 'glasswall',None))
        except Exception as error:
            assert error.args[0] == 'Replacement index 0 out of range for positional args tuple'


