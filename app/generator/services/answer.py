from common.constants import AnswerModel
from common import repository as R


class AnswerService:

    @classmethod
    def generate_answer(cls, answer_model: AnswerModel) -> str:
        if answer_model == AnswerModel.ROBERTA.value:
            return cls.run_roberta(cls)
        else:
            return ''

    def run_roberta(self) -> str:
        context = R.RESULT_PAGES[0]['content']
        return context[0:200]
