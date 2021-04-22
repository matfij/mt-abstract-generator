import os
from typing import List
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

from generator.constants import AnswerModel


class AnswerService:
    __BASE_MODEL_DIR = os.getenv('BASE_DIR') + 'generator/models/answer/'

    @classmethod
    def generate_answer(cls, phrase: str, corpus: List[str], answer_model: AnswerModel) -> str:
        cls.phrase = phrase
        cls.corpus = corpus

        if answer_model == AnswerModel.SPAN_BERT_SQUAD.value:
            return cls.run_span_bert_squad(cls, phrase, corpus)
        if answer_model == AnswerModel.ELECTRA_SQUAD.value:
            return cls.run_electra_squad(cls, phrase, corpus)
        else:
            return ''

    def run_span_bert_squad(self, phrase: str, corpus: List[str]) -> str:
        context = ''
        for text in corpus:
            context += text
        context = context.replace('-', ' ').replace(';', ' ').replace('  ', ' ')
        context_words = context.split(' ')

        context_parts = []
        current_position = 0
        maximum_sequence_length = 356  # maximum encoder length = 512
        while current_position < len(context_words):
            context_parts.append(' '.join(context_words[current_position : current_position + maximum_sequence_length]))
            current_position += maximum_sequence_length


        tokenizer = AutoTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'spanbert-finetuned-squadv1')
        model = AutoModelForQuestionAnswering.from_pretrained(self.__BASE_MODEL_DIR + 'spanbert-finetuned-squadv1')

        answer = ''
        max_score = 0
        for part in context_parts:
            try:
                inputs = tokenizer.encode_plus(phrase, part, add_special_tokens=True, return_tensors='pt')
                input_ids = inputs['input_ids'].tolist()[0]

                text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
                answer_start_scores, answer_end_scores = model(**inputs, return_dict=False)

                answer_start = torch.argmax(answer_start_scores)
                answer_end = torch.argmax(answer_end_scores) + 1

                temp_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
                temp_score = torch.max(answer_start_scores).item() + torch.max(answer_end_scores).item()

                if temp_score > max_score and 20 < len(temp_answer) < 1000:
                    answer = temp_answer
                    max_score = temp_score
            except:
                pass

        return answer

    def run_electra_squad(self, phrase: str, corpus: List[str]) -> str:
        context = ''
        for text in corpus:
            context += text
        context = context.replace('-', ' ').replace(';', ' ').replace('  ', ' ')
        context_words = context.split(' ')

        context_parts = []
        current_position = 0
        maximum_sequence_length = 356  # maximum encoder length = 512
        while current_position < len(context_words):
            context_parts.append(' '.join(context_words[current_position : current_position + maximum_sequence_length]))
            current_position += maximum_sequence_length

        tokenizer = AutoTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'electra-small-finetuned-squadv1')
        model = AutoModelForQuestionAnswering.from_pretrained(self.__BASE_MODEL_DIR + 'electra-small-finetuned-squadv1')

        answer = ''
        max_score = 0
        for part in context_parts:
            try:
                inputs = tokenizer.encode_plus(phrase, part, add_special_tokens=True, return_tensors='pt')
                input_ids = inputs['input_ids'].tolist()[0]

                text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
                answer_start_scores, answer_end_scores = model(**inputs, return_dict=False)

                answer_start = torch.argmax(answer_start_scores)
                answer_end = torch.argmax(answer_end_scores) + 1

                temp_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
                temp_score = torch.max(answer_start_scores).item() + torch.max(answer_end_scores).item()

                if temp_score > max_score and 1 < len(temp_answer) < 1000:
                    answer = temp_answer
                    max_score = temp_score
            except:
                pass

        return answer
        