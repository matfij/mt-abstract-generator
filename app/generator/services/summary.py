import os
from typing import List
import torch
from transformers import pipeline
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

from generator.constants import SummaryModel


class SummaryService:
    __BASE_MODEL_DIR = os.getenv('BASE_DIR') + 'generator/models/summary/'

    @classmethod
    def generate_summary(cls, corpus: List[str], summary_model: SummaryModel) -> str:
        if summary_model == SummaryModel.DISTILL_BART_CNN.value:
            return cls.run_distill_bart_cnn(cls, corpus)
        if summary_model == SummaryModel.DISTILL_PEGASUS_CNN.value:
            return cls.run_distill_pegasus_cnn(cls, corpus)
        else:
            return ''

    def run_distill_bart_cnn(self, corpus: List[str]) -> str:
        context = ''
        for text in corpus:
            context += text
        context = context.replace('-', ' ').replace(';', ' ').replace('  ', ' ')
        
        summarization_pipeline = pipeline('summarization', self.__BASE_MODEL_DIR + 'distill-bart-cnn')
        maximum_sequence_length = 356  # maximum encoder length = 512
        
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

    def run_distill_pegasus_cnn(self, corpus: List[str]) -> str:
        context = ''
        for text in corpus:
            context += text
        context = context.replace('-', ' ').replace(';', ' ').replace('  ', ' ')

        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = PegasusTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'distill-pegasus-cnn-16-4')
        model = PegasusForConditionalGeneration.from_pretrained(self.__BASE_MODEL_DIR + 'distill-pegasus-cnn-16-4').to(torch_device)
        maximum_sequence_length = 1024  # maximum encoder length = 2048 (?)
        
        current_position = 0
        text_words = context.split(' ')
        text_parts = []

        while current_position < len(text_words):
            if len(text_words[current_position : current_position + maximum_sequence_length]) > 200:
                text_parts.append(' '.join(text_words[current_position : current_position + maximum_sequence_length]))
            current_position += maximum_sequence_length

        summary = ''
        for text_part in text_parts:
            text_data = [text_part]
            batch = tokenizer.prepare_seq2seq_batch(text_data, truncation=True, padding='longest', return_tensors="pt").to(torch_device)
            summary_encoded = model.generate(**batch)
            summary += ' ' + tokenizer.batch_decode(summary_encoded, skip_special_tokens=True)[0]

        return summary