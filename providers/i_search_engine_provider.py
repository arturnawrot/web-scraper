from abc import ABCMeta, abstractmethod
from http_clients.i_http_client import IHttpClient
from search_engine.results import Results

class ISearchEngineProvider(object):
    __metaclass__ = ABCMeta

    def __init__(self, http_client):
        if not isinstance(http_client, IHttpClient): raise Exception('Bad interface')

        self._http_client = http_client

    @abstractmethod
    def get_results() -> Results: raise NotImplementedError