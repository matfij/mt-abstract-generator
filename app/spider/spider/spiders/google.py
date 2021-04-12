import scrapy
from googlesearch import search

from common import repository as R
from spider import config as C
from spider.spider.services.page_processing import PageProcessingSerive
from spider.spider.services.page_rating import PageRatingService


class GoogleSpider(scrapy.Spider):
    name = 'google'

    def start_requests(self):
        page_number = R.TARGET_PAGE_NUMBER
        searched_phrase = R.SEARCH_PHRASE

        result_urls = search(searched_phrase, tld="com", lang="en", num=page_number, stop=page_number)
        for ind, url in enumerate(result_urls):
            yield scrapy.Request(url)

    def parse(self, response):
        url = response.url

        references = []
        for tag in C.XPATH_HREF_TAGS:
            references.append(response.xpath(tag).getall())
        references = [ref for refs in references for ref in refs] 
        references = PageProcessingSerive.filter_references(url, references)

        content = ''
        for tag in C.XPATH_MAIN_TAGS:
            searched_xpath = tag + C.TAG_CONTENT
            content += PageProcessingSerive.clean_content(response.xpath(searched_xpath).getall())

        quality = PageRatingService.get_combined_domains_class(url, references)

        yield {
            'url': url,
            'references': references,
            'content': content,
            'quality': quality
        }

    def close(self):
        R.SPIDER_FINISHED = True
        pass
