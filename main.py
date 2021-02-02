from search_engine.search_engine import SearchEngine
from providers.bing.bing_provider import BingProvider
from http_clients.requests.requests_client import RequestsClient
from fake_useragent import UserAgent
import warnings

warnings.filterwarnings("ignore")

def search(query):
    fake_useragent = UserAgent().chrome

    headers = {
        "Agent": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": fake_useragent
    }

    http_client = RequestsClient(headers)
    search_engine_provider = BingProvider(http_client)
    search_engine = SearchEngine(search_engine_provider)

    return search_engine.get_results(query)

results = search("the lord of the rings")

print(results)