from typing import List
import spacy
import pytextrank

from generator import config as C


class ExtractService:

    @classmethod
    def extract_content(cls, corpus: List[str]) -> List[str]:
        model = spacy.load('en_core_web_md')
        text_rank = pytextrank.TextRank()
        model.add_pipe(text_rank.PipelineComponent, name='textrank', last=True)
        corpus_extract = []

        for part in corpus:
            part_summary = ''
            doc = model(part)
            
            for sentence in doc._.textrank.summary():
                if len(part_summary) + len(sentence) < C.MAX_CONTENT_LENGTH:
                    part_summary += str(sentence)

            corpus_extract.append(part_summary)

        return corpus_extract
