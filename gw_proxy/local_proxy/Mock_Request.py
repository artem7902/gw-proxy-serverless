from io import BytesIO as IO

# for now used in tests, but it might be useful to be able to intercept this
class Mock_Request:

    def __init__(self,*args, **kwargs):
        print(f'in __init__: {args} : {kwargs} ')
        
    @staticmethod
    def makefile(*args, **kwargs):
        print(f'in makefile: {args} : {kwargs} ')
        return IO(b"GET /")

    @staticmethod
    def sendall(*args, **kwargs):
       print(f'in send all: {args} : {kwargs}')