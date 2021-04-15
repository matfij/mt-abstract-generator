from typing import List

from generator.constants import AnswerModel


class AnswerService:

    @classmethod
    def generate_answer(cls, phrase: str, corpus: List[str], answer_model: AnswerModel) -> str:
        cls.phrase = phrase
        cls.corpus = corpus

        if answer_model == AnswerModel.ROBERTA.value:
            return cls.run_roberta(cls, phrase, corpus)
        else:
            return ''

    def run_roberta(self, phrase: str, corpus: List[str]) -> str:
        context = corpus[0]
        return phrase + context[0:100]
