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
        summary = ''

        if summary_model == SummaryModel.DISTILL_BART_CNN.value:
            summary = cls.run_distill_bart_cnn(cls, corpus)
        if summary_model == SummaryModel.DISTILL_PEGASUS_CNN.value:
            summary = cls.run_distill_pegasus_cnn(cls, corpus)
        
        summary = cls.clear_summary(cls, summary)
        return summary

    def clear_summary(self, summary: str) -> str:
        summary = summary.strip()
        summary = summary.replace('  ', ' ')
        
        return summary

    def run_distill_bart_cnn(self, corpus: List[str]) -> str:
        summarization_pipeline = pipeline('summarization', self.__BASE_MODEL_DIR + 'distill-bart-cnn')
        maximum_sequence_length = 356  # maximum encoder length = 512

        summary = ''
        for content in corpus:
            summary += ' ' + summarization_pipeline(content)[0]['summary_text']

        return summary

    def run_distill_pegasus_cnn(self, corpus: List[str]) -> str:
        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = PegasusTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'distill-pegasus-cnn-16-4')
        model = PegasusForConditionalGeneration.from_pretrained(self.__BASE_MODEL_DIR + 'distill-pegasus-cnn-16-4').to(torch_device)
        maximum_sequence_length = 1024  # maximum encoder length = 2048 (?)

        summary = ''
        for content in corpus:
            text_data = [content]
            batch = tokenizer.prepare_seq2seq_batch(text_data, truncation=True, padding='longest', return_tensors="pt").to(torch_device)
            summary_encoded = model.generate(**batch)
            summary += ' ' + tokenizer.batch_decode(summary_encoded, skip_special_tokens=True)[0]

        return summary
