from typing import List
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

from generator.constants import AnswerModel


class AnswerService:

    @classmethod
    def generate_answer(cls, phrase: str, corpus: List[str], answer_model: AnswerModel) -> str:
        cls.phrase = phrase
        cls.corpus = corpus

        if answer_model == AnswerModel.ROBERTA.value:
            return cls.run_bert(cls, phrase, corpus)
        else:
            return ''

    def run_bert(self, phrase: str, corpus: List[str]) -> str:
        context = ''
        for text in corpus:
            context += text

        context = context.replace('-', ' ')
        context = context.replace(';', ' ')
        context_words = context.split(' ')

        context_parts = []
        current_position = 0
        maximum_sequence_length = 356  # maximum encoder length = 512
        while current_position < len(context_words):
            context_parts.append(' '.join(context_words[current_position : current_position + maximum_sequence_length]))
            current_position += maximum_sequence_length

        tokenizer = AutoTokenizer.from_pretrained('app/generator/models/answer/bert')
        model = AutoModelForQuestionAnswering.from_pretrained('app/generator/models/answer/bert')

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
        