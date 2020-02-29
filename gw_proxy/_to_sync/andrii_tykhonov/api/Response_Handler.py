class Response_Handler():

    def __init__(self, search, replace):
        """
        Initiate a handler with `search` and `replace`. They both should
        be of type either string or list. In the case of strings the
        `search` is searched in a response and replaced by
        `replace`. In the case of list each element from `search` is
        searched in a response and replaced by an appropriate element
        from `replace`.
        """
        self.search = [search] if isinstance(search, str) else search
        self.replace = [replace] if isinstance(search, str) else replace
        if len(self.search) != len(self.replace):
            raise ValueError('Lenghts of `search` and `replace` are not equal')

    def process(self, response):
        for i, s in enumerate(self.search):
            response = response.replace(s, self.replace[i])
        return response