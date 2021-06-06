from types import resolve_bases
from django.test import TestCase
from scrapy.http import TextResponse

from spider.spider.spiders.google import GoogleSpider


class SpiderTests(TestCase):

    def setUp(self):
        self.spider = GoogleSpider()
        self.base_dir = 'spider/tests/html/'

    def test_spider_parsing(self):
        with open(self.base_dir + 'test-website-1.txt') as file: body = file.read()
        response = TextResponse(
            url='https://www.healthline.com/nutrition/',
            body=body,
            encoding='utf-8'
        )

        results = self.spider.parse(response)
        page = list(results)[0]

        self.assertEqual(len(page['content']), 5488)
        self.assertEqual(len(page['references']), 65)
    