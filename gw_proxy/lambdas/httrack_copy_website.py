import os

from osbot_aws.apis.S3 import S3
from osbot_utils.utils.Files import Files


def run(event, context):
    website_url     = event.get('website_url')
    domain_name     = website_url.replace("https://", "").replace("http://", "")
    output_folder   =  f'/tmp/{domain_name}'
    httrack_process = os.popen(f'httrack "{website_url}" -O "{output_folder}"')
    httrack_output  = httrack_process.read()
    print("httrack_output ", httrack_output)
    zipped_website  = Files.zip_folder(output_folder)
    s3_website_key = S3().file_upload(zipped_website, os.environ["S3_BUCKET_WEBSITE_COPIES"], "")
    return s3_website_key

