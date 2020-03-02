from gw_proxy.local_proxy.Server import Server


class Temp_Server:

    def __init__(self, target=None):
        self.target = target
        self.server = None

    def __enter__(self):
        self.server = Server(target=self.target).start_async()
        return self.server

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.stop()