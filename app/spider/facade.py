import crochet
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher

from common import repository as R
from spider.spider.spiders.google import GoogleSpider


# crochet.setup()


class SpiderFacade:
    crawler_runner = CrawlerRunner()

    @classmethod
    # @crochet.run_in_reactor
    def get_related_pages(cls, phrase: str, page_number: int):
        R.SEARCH_PHRASE = phrase
        R.TARGET_PAGE_NUMBER = page_number

        process = CrawlerProcess(get_project_settings())
        process.crawl(GoogleSpider)
        process.start()

        # dispatcher.connect(cls.observe_results, signal=signals.item_scraped)
        # cls.crawler_runner.crawl(GoogleSpider)

    def observe_results(self, item: dict):
        R.RESULT_PAGES.append(dict(item))
