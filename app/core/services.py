from typing import List
import crochet
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher

from common import repository as R
from core.models import AbstractModel
from spider.spider.spiders.google import GoogleSpider
from generator.facade import GeneratorFacade, AnswerModel, SummaryModel


crochet.setup()


class CoreService():
    crawler_runner = CrawlerRunner()

    @crochet.run_in_reactor
    def get_related_pages(self, phrase: str, page_number: int):
        R.RESULT_PAGES = []
        R.SPIDER_FINISHED = False
        R.SEARCH_PHRASE = phrase
        R.TARGET_PAGE_NUMBER = page_number

        dispatcher.connect(self.observe_results, signal=signals.item_scraped)
        self.crawler_runner.crawl(GoogleSpider)

    def observe_results(self, item: dict):
        R.RESULT_PAGES.append(dict(item))

    def generate_abstract(self, phrase: str, page_number: int, answer_model: AnswerModel, summary_model: SummaryModel) -> AbstractModel:
        self.get_related_pages(phrase, page_number)

        while not R.SPIDER_FINISHED:
            pass

        corpus = [page['content'] for page in R.RESULT_PAGES]
        R.RESULT_PAGES = []

        answer, summary = GeneratorFacade.generate_abstract(phrase, corpus, answer_model, summary_model)

        abstract = AbstractModel(
            answer=answer,
            summary=summary
        )

        return abstract
