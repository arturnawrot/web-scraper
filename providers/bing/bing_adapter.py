from search_engine.result import Result
from providers.bing.locators.xpath_title_locator import XPathTitleLocator
from providers.bing.locators.xpath_description_locator import XPathDescriptionLocator
from providers.bing.locators.xpath_url_locator import XPathUrlLocator
from http_clients.html_response import HtmlResponse
from providers.bing.bing_xpaths import TITLE, DESCRIPTION, URL
from lxml import etree

class BingAdapter():

    def get_results_from_html_response(self, response: HtmlResponse):
        html = response.get_contents()

        xpath_elements = self.get_xpath_records(html)

        results_list = []

        for xpath_element in xpath_elements:
            xpath_element_string = etree.tostring(xpath_element)

            try:
                results_list.append(
                    Result(
                        XPathTitleLocator(xpath_element_string).find(TITLE),
                        XPathDescriptionLocator(xpath_element_string).find(DESCRIPTION),
                        XPathUrlLocator(xpath_element_string).find(URL)
                    )
                )
            except Exception as e:
                continue

        return results_list

    def get_xpath_records(self, html):
        tree = etree.HTML(html)
        return tree.xpath('//li[@class="b_algo"]')