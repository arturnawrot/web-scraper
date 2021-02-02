from http_clients.i_response import IResponse

class Response(IResponse):

    def __init__(self, content):
        self.content = content

    def get_contents(self):
        return self.content