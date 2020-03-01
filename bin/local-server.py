import sys
sys.path.append('.')
sys.path.append('./modules/OSBOT-Utils')

from gw_proxy.local_proxy.Server import Server

if len(sys.argv)==1:
    target_server = 'https://httpbin.org'
else:
    target_server = sys.argv[1]

port=12345

print(f'***** starting proxy server for url: {target_server} on port {port}')
Server(target=target_server, port=port).setup().start()