from search_engine.title import Title
from search_engine.description import Description
from search_engine.url import Url
from search_engine.result import Result
from search_engine.results import Results
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
                        Title(XPathTitleLocator(xpath_element_string).find(TITLE)),
                        Description(XPathDescriptionLocator(xpath_element_string).find(DESCRIPTION)),
                        Url(XPathUrlLocator(xpath_element_string).find(URL))
                    )
                )
            except Exception as e:
                continue

        return Results(results_list)

    def get_xpath_records(self, html):
        tree = etree.HTML(html)
        return tree.xpath('//li[@class="b_algo"]')
    
    def get_title_from_xpath_result(self, xpath_element):
        return etree.HTML(xpath_element).xpath('//h2[1]/a[1]')

    def get_description_from_xpath_result(self, xpath_element):
        return etree.HTML(xpath_element).xpath('(//p[@class="b_paractl"]/text() | //p/strong/text() | //p//strong/text() | //p/text() | //div[@class="b_caption"]//p/*[not(@class="news_dt")] | /span[@class="aCOpRe"]/span/text() )[1]')
        
    def get_url_from_xpath_result(self, xpath_element):
        return etree.HTML(xpath_element).xpath('(//cite/a/@href | //li[@class="b_algo"]/h2/a/@href)[1]')[0]