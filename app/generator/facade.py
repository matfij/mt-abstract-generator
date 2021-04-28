from typing import List

from generator.constants import AnswerModel, SummaryModel
from generator.services.extract import ExtractService
from generator.services.answer import AnswerService
from generator.services.summary import SummaryService


class GeneratorFacade:

    @classmethod
    def generate_abstract(cls, phrase: str, corpus: List[str], answer_model: AnswerModel, summary_model: SummaryModel) -> tuple:
        corpus_extract = ExtractService.extract_content(corpus)

        answer = AnswerService.generate_answer(phrase, corpus_extract, answer_model)
        summary = SummaryService.generate_summary(corpus_extract, summary_model)

        return answer, summary
