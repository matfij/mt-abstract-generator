import os
import re
from typing import List
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

from generator import config as C
from generator.constants import AnswerModel


class AnswerService:
    __BASE_MODEL_DIR = os.getenv('BASE_DIR') + 'generator/models/answer/'
    __DISALLOWED_TOKENS = ['[SEP]', '[CLS]']

    @classmethod
    def generate_answer(cls, phrase: str, corpus: List[str], answer_model: AnswerModel) -> str:
        answer = ''

        if answer_model == AnswerModel.SPAN_BERT_SQUAD.value:
            answer = cls.run_span_bert_squad(cls, phrase, corpus)
        if answer_model == AnswerModel.ELECTRA_SQUAD.value:
            answer = cls.run_electra_squad(cls, phrase, corpus)
        
        answer = cls.clear_answer(cls, answer)
        return answer

    def clear_answer(self, answer: str) -> str:
        for token in self.__DISALLOWED_TOKENS:
            answer.replace(token, '')
        answer.strip()

        return answer

    def run_span_bert_squad(self, phrase: str, corpus: List[str]) -> str:
        tokenizer = AutoTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'spanbert-finetuned-squadv1')
        model = AutoModelForQuestionAnswering.from_pretrained(self.__BASE_MODEL_DIR + 'spanbert-finetuned-squadv1')

        answer = ''
        max_score = 0
        for content in corpus:
            try:
                inputs = tokenizer.encode_plus(phrase, content, add_special_tokens=True, return_tensors='pt')
                input_ids = inputs['input_ids'].tolist()[0]

                text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
                answer_start_scores, answer_end_scores = model(**inputs, return_dict=False)

                answer_start = torch.argmax(answer_start_scores)
                answer_end = torch.argmax(answer_end_scores) + 1

                temp_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
                temp_score = torch.max(answer_start_scores).item() + torch.max(answer_end_scores).item()

                if temp_score > max_score and C.MIN_ANSWER_LENGTH < len(temp_answer) < C.MAX_ANSWER_LENGTH:
                    answer = temp_answer
                    max_score = temp_score
            except:
                pass

        return answer

    def run_electra_squad(self, phrase: str, corpus: List[str]) -> str:
        tokenizer = AutoTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'electra-small-finetuned-squadv1')
        model = AutoModelForQuestionAnswering.from_pretrained(self.__BASE_MODEL_DIR + 'electra-small-finetuned-squadv1')

        answer = ''
        max_score = 0
        for content in corpus:
            try:
                inputs = tokenizer.encode_plus(phrase, content, add_special_tokens=True, return_tensors='pt')
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
        