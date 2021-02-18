from providers.xpath.xpath_element_locator import XPathElementLocator

class XPathBaseBingLocator(XPathElementLocator):

    def __init__(self, html):
        super().__init__(html)
    
    def find(self, xpath_queries):
        results = []
        for xpath_query in xpath_queries:
            try:
                result = self.find_xpath(xpath_query)
                
                if isinstance(result, list):
                    if len(result) > 1:
                        result = ' '.join(result)

                results.append(
                    self.find_xpath(xpath_query)
                )
            except:
                continue
        
        return self.get_best_result(results)

    def get_best_result(self, results):
        return max(results, key=len)