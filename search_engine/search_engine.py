from providers.i_search_engine_provider import ISearchEngineProvider

class SearchEngine:

    def __init__(self, provider):
        if not isinstance(provider, ISearchEngineProvider): raise Exception('Bad interface')

        self._provider = provider

    def get_results(self, query):
        return self._provider.get_results(query)