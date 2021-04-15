from typing import List
from transformers import pipeline

from generator.constants import SummaryModel


class SummaryService:

    @classmethod
    def generate_summary(cls, corpus: List[str], summary_model: SummaryModel) -> str:
        if summary_model == SummaryModel.DISTILBART.value:
            return cls.run_distilbart(cls, corpus)
        else:
            return ''

    def run_distilbart(self, corpus: List[str]) -> str:
        context = ''
        for text in corpus:
            context += text
        
        summarization_pipeline = pipeline(task='summarization', model='app/generator/models/distilbart')
        maximum_sequence_length = 512
        current_position = 0
        text_words = context.split(' ')
        text_parts = []

        while current_position < len(text_words):
            if len(text_words[current_position : current_position + maximum_sequence_length]) > 200:
                text_parts.append(' '.join(text_words[current_position : current_position + maximum_sequence_length]))
            current_position += maximum_sequence_length

        summary = ''
        for text_part in text_parts:
            summary += ' ' + summarization_pipeline(text_part)[0]['summary_text']

        return summary
