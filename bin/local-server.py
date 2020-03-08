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








# https://gofile.io/            # requires multiple servers
#
# https://wetransfer.com/       # requires email
# https://transferxl.com        # requires email
# https://free.mailbigfile.com  # uses email mode
# https://www.dropsend.com      # uses email mode
# https://www.transfernow.net   # uses email mode
# https://www.justbeamit.com/   # (very interesting concept)
# https://demo1.nextcloud.com   # POST don't work
# https://demo.pydio.com        # really good, logs in ok, byt UI doesn't work ok
# https://www.sendspace.com/    # lots of adds and sends to email
# https://www.sendfiles.net     # expired cert
# https://www.projectsend.org   # offline install
