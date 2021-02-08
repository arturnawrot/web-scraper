from lxml import etree

class XPathElementLocator():

    def __init__(self, html):
        self.html = html
        self.etree = etree.HTML(self.html)
    
    def find_xpath(self, xpath_query):
        result = self.etree.xpath(xpath_query)

        if isinstance(result, list):
            if len(result) > 1:
                result = ' '.join(result)
            elif len(result) == 1:
                result = result[0]
        
        return result
