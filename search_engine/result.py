from search_engine.title import Title
from search_engine.description import Description
from search_engine.url import Url

class Result:

    def __init__(self, title: Title, description: Description, url: Url):
        self.title = title
        self.description = description
        self.url = url
    
    def get_title(self):
        return self.title.get_title()

    def get_description(self):
        return self.description.get_description()
    
    def get_url(self):
        return self.url.get_url()