import sys
sys.path.append('.')
from gw_proxy.local_proxy.Server import Server
print(sys.path)
print("***** starting local server")

Server().setup().start()