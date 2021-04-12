from typing import List
import crochet
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher

from common.constants import AnswerModel, SummaryModel
from common import repository as R
from core.models import ResultPageModel
from spider.spider.spiders.google import GoogleSpider
from generator.generator import GeneratorFacade


crochet.setup()


class CoreService():
    '''Core application service for retrieving and processing scraped data'''
    crawler_runner = CrawlerRunner()

    @crochet.run_in_reactor
    def get_related_urls(self, phrase: str):
        R.RESULT_PAGES = []
        R.SPIDER_FINISHED = False
        R.SEARCH_PHRASE = phrase

        dispatcher.connect(self.observe_results, signal=signals.item_scraped)
        self.crawler_runner.crawl(GoogleSpider)

    def observe_results(self, item: dict):
        R.RESULT_PAGES.append(dict(item))

    def generate_abstract(self, phrase: str, answer_model: AnswerModel, summary_model: SummaryModel):
        self.get_related_urls(phrase)

        R.GENERATOR_ANSWER = ''
        R.GENERATOR_SUMMARY = ''
        R.GENERATOR_FINISHED = False

        while R.SPIDER_FINISHED == False:
            pass

        GeneratorFacade.generate_abstract(answer_model, summary_model)
