from osbot_aws.apis.S3 import S3
from osbot_aws.helpers.Lambda_Package import Lambda_Package
from osbot_aws.Globals import Globals as Osbot_Globals
from gw_proxy.Globals import Globals as Proxy_Globals


class Setup:

    def __init__(self, bot_name= None, profile_name = None, account_id=None, region_name=None, lambda_s3_bucket=None, lambda_role_name=None, lambda_layers_s3_bucket=None):
        if bot_name                 : Osbot_Globals.bot_name                 = bot_name
        if profile_name             : Osbot_Globals.aws_session_profile_name = profile_name
        if account_id               : Osbot_Globals.aws_session_account_id   = profile_name
        if region_name              : Osbot_Globals.aws_session_region_name  = region_name
        if lambda_s3_bucket         : Osbot_Globals.lambda_s3_bucket         = lambda_s3_bucket
        if lambda_role_name         : Osbot_Globals.lambda_role_name         = lambda_role_name
        if lambda_layers_s3_bucket  : Proxy_Globals.s3_bucket_lambda_layers  = lambda_layers_s3_bucket

        self.bot_name                = Osbot_Globals.bot_name
        self.profile_name            = Osbot_Globals.aws_session_profile_name
        self.region_name             = Osbot_Globals.aws_session_region_name
        self.account_id              = Osbot_Globals.aws_session_account_id
        self.s3_bucket_lambdas       = Osbot_Globals.lambda_s3_bucket
        self.lambda_role_name        = Osbot_Globals.lambda_role_name
        self.lambda_role_arn         = f"arn:aws:iam::{self.account_id}:role/{self.lambda_role_name}"
        self.lambda_layers_s3_bucket = Proxy_Globals.s3_bucket_lambda_layers
        self.s3_bucket_website_copies = Proxy_Globals.s3_bucket_website_copies

        self.s3                = S3()

    def lambda_package(self, lambda_name) -> Lambda_Package:
        lambda_package               = Lambda_Package(lambda_name)
        lambda_package.tmp_s3_bucket = self.s3_bucket_lambdas                       # these four method calls need to be refactored
        lambda_package.tmp_s3_key    = 'lambdas/{0}.zip'.format(lambda_name)
        lambda_package.aws_lambda.set_s3_bucket(lambda_package.tmp_s3_bucket)
        lambda_package.aws_lambda.set_s3_key(lambda_package.tmp_s3_key)
        return lambda_package