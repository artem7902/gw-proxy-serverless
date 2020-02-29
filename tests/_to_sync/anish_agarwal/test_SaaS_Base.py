from unittest import TestCase

from gw_proxy._to_sync.anish_agarwal.API_SaaS_VPS_Client import API_SaaS_VPS_Client


class test_SaaS_Base(TestCase):

    def setUp(self):
        super().setUp()
        self.aws_lambda = super().lambda_package('gw_bot.lambdas.gw.proxy.saas_vps')
        self.client = API_SaaS_VPS_Client()

    def test_update_lambda(self):
        self.aws_lambda.update_code()

    def test__invoke_get_directy(self):
        payload = {'path': '/', 'httpMethod': 'GET', 'headers': {'aaa': 'bbbb'}}
        self.result = self.client.request_get(payload)

    def test__invoke_get_directy__glasswall(self):
        payload = {'path': '/', 'httpMethod': 'GET', 'headers': {}, 'requestContext': {'domainPrefix': 'glasswall'} }
        self.result = self.client.request_get(payload)

    def test__invoke_get_directy__send_firefox_com(self):
        payload = {'path': '/', 'httpMethod': 'GET', 'headers': {}, 'requestContext': {'domainPrefix': 'send_firefox_com'}}
        self.result = self.client.request_get(payload)

    def test__invoke__get_via_lambda(self):
        payload = {'path': '/', 'httpMethod': 'GET', 'headers': {'aaa': 'bbbb'}}
        self.test_update_lambda()
        self.result = self.aws_lambda.invoke(payload)

    def test__invoke__get_via_lambda__glasswall(self):
        payload = {'path': '/', 'httpMethod': 'GET', 'headers': {'aaa': 'bbbb'}, 'requestContext': {'domainPrefix': 'glasswall'} }
        self.test_update_lambda()
        self.result = self.aws_lambda.invoke(payload)

    def test__invoke_post_directy(self):
        payload = {'path': '/', 'httpMethod': 'POST', 'headers': {'aaa': 'bbbb'}
                   , 'body': {'user': 'someuser', 'password': 'somepass#543'}}
        self.result = self.client.request_get(payload)

    def test__invoke_post_directy__glasswall(self):
        payload = {'path': '/', 'httpMethod': 'POST', 'headers': {},
                   'requestContext': {'domainPrefix': 'glasswall'},
                   'body': {'user': 'someuser', 'password': 'somepass#543'} }
        self.result = self.client.request_get(payload)

    def test__invoke_post_directy__send_firefox_com(self):
        payload = {'path': '/', 'httpMethod': 'POST', 'headers': {}, 'requestContext':
            {'domainPrefix': 'send_firefox_com'},
            'body': {'user': 'someuser', 'password': 'somepass#543'}}
        self.result = self.client.request_get(payload)

    def test__invoke__post_via_lambda(self):
        payload = {'path': '/', 'httpMethod': 'POST', 'headers': {'aaa': 'bbbb'}
                   , 'body': {'user': 'someuser', 'password': 'somepass#543'}}
        self.test_update_lambda()
        self.result = self.aws_lambda.invoke(payload)

    def test__invoke__post_via_lambda__glasswall(self):
        payload = {'path': '/', 'httpMethod': 'POST', 'headers': {'aaa': 'bbbb'},
                   'requestContext': {'domainPrefix': 'glasswall'}
                   , 'body': {'user': 'someuser', 'password': 'somepass#543'}}
        self.test_update_lambda()
        self.result = self.aws_lambda.invoke(payload)


