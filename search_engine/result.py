class Result:

    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url
    
    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    def get_url(self):
        return self.url