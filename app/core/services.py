from typing import List
import crochet
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher

from common import repository as R
from core.models import ResultPageModel
from spider.spider.spiders.google import GoogleSpider


crochet.setup()


class CoreService():
    '''Core application service for retrieving and processing scraped data'''
    crawler_runner = CrawlerRunner()

    @crochet.run_in_reactor
    def get_related_urls(self, phrase: str):
        R.RESULT_PAGES = []
        R.SEARCH_PHRASE = phrase
        dispatcher.connect(self.observe_results, signal=signals.item_scraped)
        self.crawler_runner.crawl(GoogleSpider)

    def observe_results(self, item: dict):
        R.RESULT_PAGES.append(dict(item))
