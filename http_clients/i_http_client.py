from abc import ABCMeta, abstractmethod
from http_clients.i_response import IResponse

class IHttpClient(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_response(self, url) -> IResponse: raise NotImplementedError