import os
import gw_proxy

from osbot_utils.utils.Files import Files
from osbot_aws.apis.S3 import S3
from osbot_aws.helpers.Lambda_Package import Lambda_Package

from gw_proxy.api.Lambda_Layer import Lambda_Layer
from gw_proxy.Globals import Globals as Proxy_Globals

from deploy.Setup import Setup

root_path = os.path.dirname(os.path.abspath(__file__))[0:-7]

class Deploy:

    def __init__(self, s3_bucket_lambdas, s3_bucket_lambda_layers, s3_bucket_website_copies):
        self.setup  = Setup()
        self.s3_bucket_lambdas = s3_bucket_lambdas if s3_bucket_lambdas else self.setup.s3_bucket_lambdas
        self.s3_bucket_lambda_layers = s3_bucket_lambda_layers if s3_bucket_lambda_layers else self.setup.lambda_layers_s3_bucket
        self.s3_bucket_website_copies = s3_bucket_website_copies if s3_bucket_website_copies else self.setup.s3_bucket_website_copies

    def get_lambda_package(self, lambda_name, env_variables, lambda_layers, lambda_role_arn):
        package = Lambda_Package(lambda_name)
        lambda_role_arn   = lambda_role_arn if lambda_role_arn else self.setup.lambda_role_arn

        package.aws_lambda.set_s3_bucket(self.s3_bucket_lambdas) \
                          .set_role(lambda_role_arn)\
                          .set_env_variables(env_variables)\
                          .set_layers(lambda_layers)
        return package

    def deploy_lambda__httrack_copy_website(self, lambda_name='gw_proxy.lambdas.httrack_copy_website', httrack_layer_version_arn=None, lambda_role_arn=None):
        env_variables = {"S3_BUCKET_WEBSITE_COPIES" : self.s3_bucket_website_copies}
        package = self.get_lambda_package(lambda_name, env_variables, [httrack_layer_version_arn], lambda_role_arn)
        package.create()
        source_file = f'{root_path}/gw_proxy/lambdas/httrack_copy_website.py'
        package.add_file(source_file)
        package.aws_lambda.handler = 'httrack_copy_website.run'
        package.update()
        return package


    def deploy_lambda_layer_glasswall_editor(self):
        source_path = os.path.dirname(gw_proxy.__file__)[0:-8] + "modules/sdk-eval-toolset/libraries/linux"
        folders_mapping = {source_path: 'lib/sdk-eval-toolset'}
        version_arn = Lambda_Layer(name="glasswall_editor_engine", folders_mapping=folders_mapping,
                     s3_bucket=self.s3_bucket_lambda_layers).create()
        return version_arn

    def deploy_lambda_layer_httrack(self):
        S3().file_download_to(Proxy_Globals.s3_bucket_httrack_lambda_layer_sources, "httrack.zip",
                                                        f'{root_path}/gw_proxy/layers/httrack.zip')
        Files.folder_delete_all(f'{root_path}/gw_proxy/layers/httrack')
        Files.unzip_file(f'{root_path}/gw_proxy/layers/httrack.zip', f'{root_path}/deploy_tmp')
        Files.delete(f'{root_path}/gw_proxy/layers/httrack.zip')
        source_path = f'{root_path}/deploy_tmp/httrack'
        folders_mapping = {source_path: ''}
        version_arn = Lambda_Layer(name="httrack", folders_mapping=folders_mapping,
                     s3_bucket=self.s3_bucket_lambda_layers).create()
        return version_arn