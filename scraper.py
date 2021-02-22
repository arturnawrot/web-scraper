from search_engine.search_engine import SearchEngine
from providers.bing.bing_provider import BingProvider
from http_clients.requests.requests_client import RequestsClient
from fake_useragent import UserAgent
import warnings

warnings.filterwarnings("ignore")

def search(query):
    tries = 0

    while tries < 3:
        fake_useragent = UserAgent().chrome

        headers = {
            "Content-Type": "text/html; charset=utf-8",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            # "Accept-Encoding": "gzip, deflate, br", <-- For some reason it breaks the request
            "Connection": "keep-alive",
            "Cache-Control": "no-cache",
            "User-Agent": fake_useragent
        }

        http_client = RequestsClient(headers)
        search_engine_provider = BingProvider(http_client)
        search_engine = SearchEngine(search_engine_provider)

        results = search_engine.get_results(query)

        if len(results) == 0:
            tries += 1
            continue
        else:
            break
    
    return results

