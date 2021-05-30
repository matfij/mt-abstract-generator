import os
from typing import List
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

from generator import config as C
from generator.constants import AnswerModel


class AnswerService:
    __BASE_MODEL_DIR = os.getenv('BASE_DIR') + 'generator/models/answer/'
    __DISALLOWED_TOKENS = ['[SEP]', '[CLS]']

    @classmethod
    def generate_answer(cls, phrase: str, corpus: List[str], answer_model: AnswerModel) -> str:
        bert_answer = cls.run_span_bert_squad(cls, phrase, corpus)
        electra_answer = cls.run_electra_squad(cls, phrase, corpus)

        if bert_answer.lower() in electra_answer.lower():
            answer = cls.clear_answer(cls, electra_answer, phrase)
        elif electra_answer.lower() in bert_answer.lower():
            answer = cls.clear_answer(cls, bert_answer, phrase)
        else:
            answer = cls.clear_answer(cls, electra_answer, phrase) + ' ' + cls.clear_answer(cls, bert_answer, phrase)

        answer = answer.strip()
        return answer

    def clear_answer(self, answer: str, phrase: str) -> str:
        if phrase.lower() in answer.lower():
            answer = answer[len(phrase):]

        for token in self.__DISALLOWED_TOKENS:
            answer = answer.replace(token, '')
        answer = answer.strip()

        if len(answer) > 0 and answer[len(answer) - 1] != '.': answer += '.'

        answer = answer.capitalize()

        return answer

    def run_span_bert_squad(self, phrase: str, corpus: List[str]) -> str:
        tokenizer = AutoTokenizer.from_pretrained(self.__BASE_MODEL_DIR + 'spanbert-finetuned-squadv1')
        model = AutoModelForQuestionAnswering.from_pretrained(self.__BASE_MODEL_DIR + 'spanbert-finetuned-squadv1')

        max_sequence_length = 3 * 512

        corpus_parts = ['']
        part_counter = 0
        for part in corpus:
            if len(corpus_parts[part_counter]) < max_sequence_length:
                corpus_parts[part_counter] += part
            else:
                part_counter += 1
                corpus_parts.append(part)

        answer = ''
        max_score = 0
        for content in corpus_parts:
            try:
                inputs = tokenizer.encode_plus(phrase, content, add_special_tokens=True, return_tensors='pt')
                input_ids = inputs['input_ids'].tolist()[0]

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

        max_sequence_length = 3 * 512
        
        corpus_parts = ['']
        part_counter = 0
        for part in corpus:
            if len(corpus_parts[part_counter]) < max_sequence_length:
                corpus_parts[part_counter] += part
            else:
                part_counter += 1
                corpus_parts.append(part)

        answer = ''
        max_score = 0
        for content in corpus_parts:
            try:
                inputs = tokenizer.encode_plus(phrase, content, add_special_tokens=True, return_tensors='pt')
                input_ids = inputs['input_ids'].tolist()[0]

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
