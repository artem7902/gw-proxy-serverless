
from http import HTTPStatus

from gw_proxy._to_sync.andrii_tykhonov.api.Response_Handler import Response_Handler
from gw_proxy._to_sync.andrii_tykhonov.api.proxy import Proxy

so_resp_handler = Response_Handler(
    'Stack Overflow', '<b>[CHANGED BY THE PROXY]</b>')

pre_order = (
    'Product available for pre-order at the '
    '<a href="http://glasswall-store.com/">Glasswall Store</a>'
)
gws_resp_handler = Response_Handler(
    [
        'glasswallsolutions.com',
        ('We have partnered with Royal Airforce and Royal Navy to '
         'take STEM to The Belvedore Academy in Liverpool'),
        ('The move comes as the US car giant retreats from '
         'more markets to focus on more profitable countries.'),
    ],
    [
        'glasswall.gw-proxy.com',
        pre_order,
        pre_order,
    ]
)


def run(event, context):
    try:
        proxy_map = {
            'stackoverflow': ['https://stackoverflow.com', so_resp_handler],
            'glasswall': [
                'https://www.glasswallsolutions.com', gws_resp_handler],
            'gw-proxy': [
                'https://glasswall-file-drop.azurewebsites.net', None],
        }
        path = event.get('path', '')
        domain_prefix = event.get(
            'requestContext', {}).get('domainPrefix', 'gw-proxy')
        item = proxy_map.get(domain_prefix)
        if item is None:
            item = [f'https://{domain_prefix.replace("_", ".")}', None]
        url = item[0]
        proxy = Proxy(f'{url}{path}')
        return proxy.handle_request(event, response_handler=item[1])
    except Exception as error:
        message = f'[gw_proxy] {error}'
        #log_error('Error in Lambda', {'text': message})
        return {
            'error' : message,
            'statusCode': HTTPStatus.INTERNAL_SERVER_ERROR.value,
        }