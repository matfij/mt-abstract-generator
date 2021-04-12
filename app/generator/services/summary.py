from common.constants import SummaryModel
from common import repository as R


class SummaryService:

    @classmethod
    def generate_summary(cls, summary_model: SummaryModel) -> str:
        if summary_model == SummaryModel.DISTILBART.value:
            return cls.run_distilbart(cls)
        else:
            return ''

    def run_distilbart(self) -> str:
        context = R.RESULT_PAGES[0]['content']
        return context
