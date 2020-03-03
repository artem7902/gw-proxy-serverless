import hashlib
import os
import sys
sys.path.append('/home/runner/work/gw-proxy-serverless/gw-proxy-serverless/modules/OSBot-AWS')
sys.path.append('/home/runner/work/gw-proxy-serverless/gw-proxy-serverless/modules/OSBot-Utils')
sys.path.append('/home/runner/work/gw-proxy-serverless/gw-proxy-serverless/modules/OSBot-python-utils')
sys.path.append('.')

from osbot_aws.apis.IAM import IAM
from osbot_aws.apis.S3 import S3

from deploy.Deploy import Deploy
from gw_proxy.Globals import Globals as Proxy_Globals

GITHUB_REPOSITORY_MAIN = 'filetrust/gw-proxy-serverless'
GITHUB_REPOSITORY      = os.environ['GITHUB_REPOSITORY']
GITHUB_REF             = os.environ['GITHUB_REF']

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))[0:-7]

if not os.path.exists(f'{ROOT_PATH}/gw_proxy/layers'):
    os.mkdir(f'{ROOT_PATH}/gw_proxy/layers')
if not os.path.exists(f'{ROOT_PATH}/deploy_tmp'):
    os.mkdir(f'{ROOT_PATH}/deploy_tmp')

# Create S3 buckets for the repo/branch if needed

if not GITHUB_REPOSITORY == GITHUB_REPOSITORY_MAIN:
    REPO_OWNER_NAME = GITHUB_REPOSITORY.split("/", 1)[0]
    BRANCH_HASH     = hashlib.md5(GITHUB_REF.encode()).hexdigest()[:10] if not GITHUB_REF=="refs/heads/master" else ""
    s3_bucket_lambdas        = f'gw-proxy-lambdas-{REPO_OWNER_NAME}-{BRANCH_HASH}' if GITHUB_REPOSITORY else '' # must be unique in AWS
    s3_bucket_lambda_layers  = f'gw-proxy-lambda-layers-{REPO_OWNER_NAME}-{BRANCH_HASH}' if GITHUB_REPOSITORY else '' # must be unique in AWS
    s3_bucket_website_copies = f'gw-proxy-website-copies-{REPO_OWNER_NAME}-{BRANCH_HASH}' if GITHUB_REPOSITORY else '' # must be unique in AWS
    deployment_buckets = (s3_bucket_lambdas, s3_bucket_lambda_layers,s3_bucket_website_copies)
    for bucket in deployment_buckets:
        if not S3().bucket_exists(bucket):
            bucket_create_result = S3().bucket_create(bucket, Proxy_Globals.aws_session_region_name)
            print(bucket + " bucket_create_result: " + bucket_create_result.get('data'))


# Create deploy object
deploy = Deploy(s3_bucket_lambdas, s3_bucket_lambda_layers, s3_bucket_website_copies)

# Deploy lambda layers
lambda_layer_version_arn_httrack          = deploy.deploy_lambda_layer_httrack()
#lambda_layer_version_arn_glasswall_editor = deploy.deploy_lambda_layer_glasswall_editor()

# Create IAM roles for lambdas
assume_policy_document = {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "lambda.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
}
policy_document__httrack_copy_website = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": f'arn:aws:s3:::{s3_bucket_website_copies}/*'
        }
    ]
}
lambda_iam__httrack_copy_website = IAM(role_name="gw-proxy-httrack-copy-website-lambda-role")
if not lambda_iam__httrack_copy_website.role_exists():
    lambda_iam__httrack_copy_website.role_create(assume_policy_document)
policy_arn__httrack_copy_website = lambda_iam__httrack_copy_website.policy_create(policy_name = 'gw-proxy-httrack-copy-website-lambda-policy',
                                               policy_document= policy_document__httrack_copy_website,
                                               delete_before_create=True).get('policy_arn')
lambda_iam__httrack_copy_website.role_policy_attach(policy_arn__httrack_copy_website)

# Deploy lambdas
deploy.deploy_lambda__httrack_copy_website(httrack_layer_version_arn=lambda_layer_version_arn_httrack, lambda_role_arn=lambda_iam__httrack_copy_website.role_arn())