import re
from typing import List

from spider.spider.services.page_processing import PageProcessingSerive


class PageRatingService:

    @classmethod
    def get_domain(self, url: str) -> str:
        protocol_ind = url.index('//') + 2
        if protocol_ind:
            url = url[protocol_ind:]
            post_domain_ind = url.index('/')
            url = url[:post_domain_ind]
            pre_domain_ind = ''.join(url).rindex('.') + 1
            domain = url[pre_domain_ind:]
            return domain
        else:
            return ''

    @classmethod
    def get_combined_domains_class(self, url: str, references: List[str]) -> float:
        desired_domains = [
            'org', 'int', 'edu', 'gov', 'mil', 'eu', 'us', 'wiki', 'review'
        ]
        average_domains = [
            'com', 'net', 'ai', 'au', 'ca', 'academy', 'cern', 'clinic', 'codes', 'health',
            'management', 'media', 'mobi', 'tech', 'technology', 'study', 'co'
        ]
        page_domain = self.get_domain(url)

        combained_domains_class = 0
        if any(page_domain == desired_domain for desired_domain in desired_domains):
            combained_domains_class += 50
        elif any(page_domain == average_domain for average_domain in average_domains):
            combained_domains_class += 30
        else:
            combained_domains_class -= 10

        for ref in references:
            gain = 1

            if True in [(ref_part in page_domain) for ref_part in ref.split('.')]:
                gain = 0.1
            try:
                if sum(PageProcessingSerive.get_url_body(ref) in h for h in references) > 1:
                    gain = 0.1
            except:
                pass

            if any(desired_domain in ref for desired_domain in desired_domains):
                gain *= 5
            elif any(average_domain in ref for average_domain in average_domains):
                gain *= 2
            else:
                gain *= -3

            combained_domains_class += gain

        return combained_domains_class
