from common import repository as R


class GeneratorFacade:

    @classmethod
    def generate_abstract(self):
        R.GENERATOR_ANSWER = 'go on a diet'
        R.GENERATOR_SUMMARY= 'go on a strict diet, eat fewer calories, burn more fat'
        R.GENERATOR_FINISHED = True
