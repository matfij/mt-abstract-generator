from django.test import TestCase

from spider import config as C
from spider.spider.services.page_rating import PageRatingService


class RatingTests(TestCase):

    def test_get_url_domain(self):
        url = 'http://matfij.gitlab.io/abstract-generator-client/home'

        domain = PageRatingService.get_domain(url)

        self.assertEqual('io', domain)

    def test_page_rating(self):
        url = 'https://www.calu.edu/'
        references = [
            'http://www.calvulcans.com/',
            'https://www.facebook.com/CalUofPA/',
            'https://www.youtube.com/user/CalUofPA',
            'https://www.twitter.com/CalUofPA',
            'https://www.linkedin.com/school/35882/',
            'https://calvulcans.com/',
            'https://secure.ethicspoint.com/domain/media/en/gui/37117/index.html',
            'http://www.passhe.edu/'
        ]

        rating = PageRatingService.get_combined_domains_class(url, references)

        self.assertEqual(71.4, rating)

    def test_getting_best_pages(self):
        pages = [
            {
                'page_url': 'https://en.wikipedia.org/wiki/Robotics',
                'quality': 90,
                'content': 'o' * 100000
            },
            {
                'page_url': 'https://www.mtsu.edu/programs/mechatronics/',
                'quality': 70,
                'content': 'o' * 100000
            },
            {
                'page_url': 'https://en.wikipedia.org/wiki/Robotics',
                'quality': 80,
                'content': 'o' * 100000
            }
        ]

        best_pages = PageRatingService.get_best_pages(pages)
        best_pages_content_length = sum(len(page['content']) for page in best_pages)

        self.assertLess(best_pages_content_length, C.TOTAL_CONTENT_MAX_LIMIT)
        self.assertTrue(pages[0] in best_pages)
        self.assertTrue(pages[1] in best_pages)
        self.assertTrue(pages[2] not in best_pages)