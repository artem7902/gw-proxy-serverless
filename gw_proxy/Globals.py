class Globals:
    aws_session_region_name                = 'eu-west-1'          #'eu-west-1'
    s3_bucket_lambda_layers                = 'gw-proxy-lambda-layers'     # must be unique in AWS
    s3_bucket_website_copies               = 'gw-proxy-website-copies'     # must be unique in AWS
    s3_bucket_httrack_lambda_layer_sources  = 'httrack-lambda-layer'