import requests
from http_clients.html_response import HtmlResponse
from http_clients.i_http_client import IHttpClient

class RequestsClient(IHttpClient):

    def __init__(self, headers, response_type='html'):
        self.client = requests
        self.headers = headers
        self.response_type = response_type

    def get(self, url):
        content = self.client.get(url, headers=self.headers).content
        
        if self.response_type == 'html':
            return HtmlResponse(content)
        
        raise Exception('Unknown response type')