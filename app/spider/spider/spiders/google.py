import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'

    def start_requests(self):
        page_number = 10
        searched_phrase = 'How to get fit?'

        result_urls = search(searched_phrase, tld="com", lang="en", num=page_number, stop=page_number)
        for ind, url in enumerate(result_urls):
            yield scrapy.Request(url)

    def parse(self, response):
        page_url = response.url

        yield {
            'page_url': page_url
        }

    def close(self):
        # TODO - notify django
        pass
