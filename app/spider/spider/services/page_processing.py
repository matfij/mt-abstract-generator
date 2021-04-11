from typing import List


class PageProcessingSerive:

    @classmethod
    def filter_references(self, url: str, references: List[str]) -> List[str]:
        url_body = self.get_url_body(url)
        valid_references = []

        for ref in references:
            if not ref.find('http') and url_body != None and ref not in url_body:
                valid_references.append(ref)

        return valid_references

    @classmethod
    def get_url_body(self, url: str) -> str:
        if '//' in url:
            protocol_ind = url.rindex('//') + 2
            if protocol_ind:
                url = url[protocol_ind:]
                if '/' in url:
                    post_domain_ind = url.index('/')
                    url = url[:post_domain_ind]
                pre_domain_ind = ''.join(url).rindex('.')
                url = url[:pre_domain_ind]
                if 'www.' in url:
                    www_ind = url.index('www.') + 4
                    if www_ind:
                        return url[www_ind:]
                else:
                    return url
            else:
                return None
        else:
            return None
