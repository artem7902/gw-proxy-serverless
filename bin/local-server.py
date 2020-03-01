import sys
sys.path.append('.')
sys.path.append('./modules/OSBOT-Utils')
from gw_proxy.local_proxy.Server import Server

print("***** starting local server")
Server(port=12345).setup().start()