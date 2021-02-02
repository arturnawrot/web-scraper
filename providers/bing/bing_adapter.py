from search_engine.title import Title
from search_engine.description import Description
from search_engine.url import Url
from search_engine.result import Result
from search_engine.results import Results
from http_clients.html_response import HtmlResponse
from lxml import etree

class BingAdapter():

    def get_results_from_html_response(self, response: HtmlResponse):
        html = response.get_contents()

        xpath_elements = self.get_xpath_records(html)

        results_list = []

        for xpath_element in xpath_elements:
            xpath_element_string = etree.tostring(xpath_element)

            results_list.append(
                Result(
                    Title(self.get_title_from_xpath_result(xpath_element_string)),
                    Description(self.get_description_from_xpath_result(xpath_element_string)),
                    Url(self.get_url_from_xpath_result(xpath_element_string))
                )
            )

        return Results(results_list)

    def get_xpath_records(self, html):
        tree = etree.HTML(html)
        return tree.xpath('//li[@class="b_algo"]')
    
    def get_title_from_xpath_result(self, xpath_element):
        return etree.HTML(xpath_element).xpath('//h2[1]/a[1]')[0].text

    def get_description_from_xpath_result(self, xpath_element):
        return etree.HTML(xpath_element).xpath('//p[@class="b_paractl"][1]')[0].text

    def get_url_from_xpath_result(self, xpath_element):
        return etree.HTML(xpath_element).xpath('//cite[1]')[0].text