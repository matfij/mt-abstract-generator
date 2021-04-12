import re
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

    @classmethod
    def clean_content(self, spans: List[str]) -> str:
        content = ''
        for span in spans:
            if len(span) > 100:
                content += ' ' + span
        content = content.replace('  ', ' ')
        
        filler_tokens = [
            u"\n", u"\t", u"\r", u"\"", "  ", "    ",
            '+', '<', '[', ',', '>', ']', '&', '—', '}', '{', '|', '‘', '=', '~', '(', '/', '~', ')', '..', '@', '#', '$', '*', ',,',
            '--', '...', ';', ':', '^'
        ]
        for token in filler_tokens:
            content = content.replace(token, '')

        filler_patterns = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE
        )
        content = filler_patterns.sub(r'', content)

        return content
