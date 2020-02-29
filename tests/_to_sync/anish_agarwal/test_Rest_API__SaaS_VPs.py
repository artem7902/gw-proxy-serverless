# this call and methods contain the multiple bits required to set up the proxy (todo: consolidate in one end-to-end
#  solution to be executed on a clear AWS region/organisation)
class test_Rest_API__SaaS_VPs(Test_Helper):

    def setUp(self):
        super().setUp()
        self.api_name    = 'lambda-proxy'
        self.lambda_name = 'gw_bot_lambdas_gw_proxy_saas_vps'
        self.api_gateway = API_Gateway()

    def test_setup_lambda_route(self):                      # will create a {proxy+} integration
        rest_api    = Rest_API(self.api_name).create()
        parent_id = rest_api.resource_id('/')
        rest_api.api_gateway.resource_create(rest_api.id(),parent_id,'{proxy+}')
        self.result = rest_api.add_method_lambda('/'        , 'ANY', self.lambda_name)  # need to add both
        self.result = rest_api.add_method_lambda('/{proxy+}', 'ANY', self.lambda_name)  # since this one wasn't catching the root requests
        rest_api.deploy()
        #self.result = rest_api.test_method('/','GET')

    def test_deploy_api(self):
        rest_api = Rest_API(self.api_name).create()
        self.result = rest_api.deploy()

    # here is the test that added the A record for both top level domain and child domains
    # def test_record_set_upsert(self):
    #
    #     name                = 'gw-proxy.com.'
    #     record_type         = 'A'
    #     dns_name            = 'd-noho75bpih.execute-api.eu-west-1.amazonaws.com.'
    #     hosted_zone_id      = '/hostedzone/ZMHOWKWA1ZN69'
    #     alias_hosted_zone_id = 'ZLY8HYME6SFDD'
    #     self.result = Route_53().record_set_upsert(name, record_type, dns_name,hosted_zone_id,alias_hosted_zone_id)
    #
    # def test_record_set_upsert(self):
    #     from osbot_aws.apis.Route_53 import Route_53
    #     name                = '*.gw-proxy.com.'
    #     record_type         = 'A'
    #     dns_name            = 'd-noho75bpih.execute-api.eu-west-1.amazonaws.com.'
    #     hosted_zone_id      = '/hostedzone/ZMHOWKWA1ZN69'
    #     alias_hosted_zone_id = 'ZLY8HYME6SFDD'
    #     self.result = Route_53().record_set_upsert(name, record_type, dns_name,hosted_zone_id,alias_hosted_zone_id)
    #
    # # here is the test that asked for the wildcart Cert to be created
    # def test_certificate_request(self):
    #     #self.result = self.acm.certificate_request('*.gw-proxy.com')
    #     self.result = self.acm.certificate('arn:aws:acm:eu-west-1:311800962295:certificate/1f191c3a-0214-4ef5-9f03-27cc0b46bef3')
    #
    # def test_GET_request(self):
    #     self.result = GET(Rest_API(self.api_name).url())
    #
    # # adding domain to API Gateway
    # # gw-proxy.com
    # def test_domain_name_add_path_mapping(self):
    #     rest_api_id = self.api_gateway.rest_api_id('lambda-proxy')
    #     domain_name = 'gw-proxy.com'
    #     base_path   = ''
    #     self.result = self.api_gateway.domain_name_add_path_mapping(rest_api_id=rest_api_id,domain_name=domain_name,base_path=base_path)
    #
    # def test_domain_name_create(self):
    #     domain_name     = 'gw-proxy.com'
    #     certificate_arn = 'arn:aws:acm:eu-west-1:311800962295:certificate/cac6ccbe-e5a6-41b1-ab87-461ff1d88458'
    #     self.result     = self.api_gateway.domain_name_create__regional(domain_name=domain_name, certificate_arn=certificate_arn)
    #
    # # *.gw-proxy.com
    #
    # def test_domain_name_create(self):
    #     domain_name     = '*.gw-proxy.com'
    #     certificate_arn = 'arn:aws:acm:eu-west-1:311800962295:certificate/be75edef-b698-4425-bf7a-7a129bb0331e'
    #     self.result     = self.api_gateway.domain_name_create__regional(domain_name=domain_name, certificate_arn=certificate_arn)
    #
    # def test_domain_name_add_path_mapping(self):
    #     rest_api_id = self.api_gateway.rest_api_id('lambda-proxy')
    #     domain_name = '*.gw-proxy.com'
    #     base_path   = ''
    #     self.result = self.api_gateway.domain_name_add_path_mapping(rest_api_id=rest_api_id,domain_name=domain_name,base_path=base_path)