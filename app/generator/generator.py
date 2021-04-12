from common.constants import AnswerModel, SummaryModel
from common import repository as R
from generator.services.answer import AnswerService
from generator.services.summary import SummaryService


class GeneratorFacade:

    @classmethod
    def generate_abstract(cls, answer_model: AnswerModel, summary_model: SummaryModel):
        R.GENERATOR_ANSWER = AnswerService.generate_answer(answer_model)
        R.GENERATOR_SUMMARY= SummaryService.generate_summary(summary_model)
        R.GENERATOR_FINISHED = True
