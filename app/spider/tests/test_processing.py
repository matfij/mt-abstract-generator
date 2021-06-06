from django.test import TestCase

from spider.spider.services.page_processing import PageProcessingSerive


class ProcessingTests(TestCase):

    def test_reference_filtering(self):
        page_url = 'https://en.wikipedia.org/wiki/Mechatronics'
        reference_urls = [
            'http://www.ieee-asme-mechatronics.org/',
            'https://data.bnf.fr/ark:/12148/cb119850628',
            'https://en.wikipedia.org/wiki/Mechatronics',
            'https://az.wikipedia.org/wiki/Mexatronika',
            'https://pl.wikipedia.org/wiki/Robotyka'
        ]

        filtered_urls = PageProcessingSerive.filter_references(page_url, reference_urls)

        self.assertNotEqual(page_url in filtered_urls, True)
        self.assertEqual(len(filtered_urls), 2)

    def test_get_url_body(self):
        url = 'http://matfij.gitlab.io/abstract-generator-client/home'

        body = PageProcessingSerive.get_url_body(url)

        self.assertEqual('matfij.gitlab', body)

    def test_content_cleaning(self):
        junk_spans = [
            'We look forward to your questions via WhatsApp!',
            'Please enable Javascript for a better experience.',
            '&quot;&quot;&quot;Descriptor for TestCase.multi_db ><><><><><><><><><><><><><><><><><> deprecation.&quot;&quot;&quot; &quot;&quot;&quot;Descriptor for TestCase.multi_db',
            '©2021 Mateusz Fijak'
        ]
        quality_spans = [
            'Independent of Frameworks. The architecture does not depend on the existence of some library of feature laden software. This allows you to use such frameworks as tools, rather than having to cram your system into their limited constraints.',
            'Testable. The business rules can be tested without the UI, Database, Web Server, or any other external element.',
            'Independent of UI. The UI can change easily, without changing the rest of the system. A Web UI could be replaced with a console UI, for example, without changing the business rules.'
        ]
        full_content = ''.join(junk_spans + quality_spans)
        quality_content = ''.join(quality_spans)

        cleaned_content = PageProcessingSerive.clean_content(junk_spans + quality_spans)
        # print('\n\n\nCLEANED: \n\n', cleaned_content, '\n\n')

        self.assertLess(len(cleaned_content), len(full_content))
        self.assertTrue(0.9*len(quality_content) < len(cleaned_content) < 1.1*len(quality_content))
        for span in junk_spans:
            self.assertFalse(span.lower().strip() in cleaned_content.lower().strip())
        for span in quality_spans:
            self.assertTrue(span.lower().strip() in cleaned_content.lower().strip())

        