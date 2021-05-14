import scrapy
from googlesearch import search

from common import repository as R
from spider import config as C
from spider.spider.services.page_processing import PageProcessingSerive
from spider.spider.services.page_rating import PageRatingService


class GoogleSpider(scrapy.Spider):
    name = 'google'

    def start_requests(self):
        page_number = min(max(C.MIN_PAGE_NUMBER, R.TARGET_PAGE_NUMBER), C.MAX_PAGE_NUMBER)
        searched_phrase = R.SEARCH_PHRASE

        result_urls = search(searched_phrase, num=page_number, stop=page_number, pause=0.0)
        for url in result_urls:
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

        if (C.CONTENT_MIN_LIMIT < len(content) < C.CONTENT_MAX_LIMIT):
            yield {
                'url': url,
                'references': references,
                'quality': quality,
                'content': content
            }

    def close(self):
        R.RESULT_PAGES = PageRatingService.get_best_pages(R.RESULT_PAGES)
        R.SPIDER_FINISHED = True
