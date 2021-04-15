from typing import List

from generator.constants import AnswerModel, SummaryModel
from generator.services.answer import AnswerService
from generator.services.summary import SummaryService


class GeneratorFacade:

    @classmethod
    def generate_abstract(cls, phrase: str, corpus: List[str], answer_model: AnswerModel, summary_model: SummaryModel) -> tuple:
        answer = AnswerService.generate_answer(phrase, corpus, answer_model)
        summary = SummaryService.generate_summary(corpus, summary_model)

        return answer, summary
