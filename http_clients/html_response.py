from http_clients.response import Response
from utils import is_html

class HtmlResponse(Response):

    def __init__(self, content):
        if is_html(content) is False: raise Exception('Provided response is not an HTML format.')

        super().__init__(content)