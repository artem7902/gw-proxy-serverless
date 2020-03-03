import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE_DIR, 'modules')

sys.path.append(BASE_DIR)
for d in os.listdir(MODULES_DIR):
    sys.path.append(os.path.join(MODULES_DIR, d))

from gw_proxy.local_proxy.Server import Server

target_server = 'https://httpbin.org'
port          = 12345

if len(sys.argv) == 2:
    target_server = sys.argv[1]
elif len(sys.argv)==3:
    target_server = sys.argv[1]
    port          = int(sys.argv[2])



print(f'***** starting proxy server for url: {target_server} on port {port}')
Server(target=target_server, port=port).setup().start()


# https://demo.pydio.com        # really good by doesn't load ok
# https://demo1.nextcloud.com   # POST don't work


# https://www.transfernow.net
# https://www.projectsend.org
# https://www.dropsend.com
# https://transferxl.com
# https://www.sendfiles.net
# https://free.mailbigfile.com/
# https://www.justbeamit.com/  (very interresting concept)
# https://www.sendspace.com/

