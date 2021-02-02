from providers.i_search_engine_provider import ISearchEngineProvider
from providers.bing.bing_adapter import BingAdapter

class BingProvider(ISearchEngineProvider):

    ROOT_URL = 'https://www.bing.com/search'

    def __init__(self, http_client):
        super().__init__(http_client)

        self.adapter = BingAdapter()
    
    def get_results(self, query):
        query = self.ROOT_URL + '?q=' + query
        html_response = self._http_client.get(query)
        return self.adapter.get_results_from_html_response(html_response)