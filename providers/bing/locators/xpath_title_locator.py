from providers.bing.locators.xpath_base_bing_locator import XPathBaseBingLocator

class XPathTitleLocator(XPathBaseBingLocator):

    def __init__(self, html):
        super().__init__(html)