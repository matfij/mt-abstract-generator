import os
from typing import List
import spacy
import pytextrank

from generator import config as C


class ExtractService:

    @classmethod
    def extract_content(cls, phrase: str, corpus: List[str]) -> List[str]:
        model = spacy.load('en_core_web_md')
        text_rank = pytextrank.TextRank()
        model.add_pipe(text_rank.PipelineComponent, name='textrank', last=True)

        corpus_extract = []

        for part in corpus:
            part_summary = ''
            doc = model(phrase + ' ' + part)
            doc_len_max = round(0.8*len(doc))
            doc_len_min = round(0.2*len(doc))
            
            for sentence in doc._.textrank.summary():
                if len(part_summary) + len(sentence) < min(doc_len_max, C.MAX_CONTENT_LENGTH):
                    part_summary += ' ' + str(sentence)

            if len(part_summary) > min(doc_len_min, C.MIN_CONTENT_LENGTH):
                part_summary = part_summary.strip()
                corpus_extract.append(part_summary)

        if int(os.getenv('WRITE_FILES', default=0)) == 1:
            cls.save_data(cls, corpus, corpus_extract)

        return corpus_extract

    def save_data(self, pages: List[str], abstracts: List[str]):
        with open('extracts.json', 'w') as file:
            file.write(str(abstracts))

        with open('corpus.json', 'w') as file:
            file.write(str(pages))
