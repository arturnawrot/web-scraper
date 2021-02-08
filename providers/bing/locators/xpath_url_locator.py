from providers.bing.locators.xpath_base_bing_locator import XPathBaseBingLocator

class XPathUrlLocator(XPathBaseBingLocator):

    def __init__(self, html):
        super().__init__(html)