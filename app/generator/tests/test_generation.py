import json
from unittest.case import skipIf
from django.test import TestCase

from generator import config as C
from generator.constants import AnswerModel
from generator.constants import SummaryModel
from generator.services.extract import ExtractService
from generator.services.answer import AnswerService 
from generator.services.summary import SummaryService 


class GeneratorTests(TestCase):

    def setUp(self):
        self.base_dir = 'generator/tests/mocks/'

        with open(self.base_dir + 'pages.json', 'r') as file:
            self.pages = json.loads(file.read())

        with open(self.base_dir + 'extracts.json', 'r') as file:
            self.extracts = json.loads(file.read())

    def test_extract_generation(self):
        phrase = 'Microkernel Architecture'
        corpus = [page['corpus'] for page in self.pages]

        extracts = ExtractService.extract_content_textrank(phrase, corpus)

        self.assertEqual(len(extracts), len(corpus))
        for extract in extracts:
            self.assertGreater(len(extract), C.MIN_CONTENT_LENGTH)
            self.assertLess(len(extract), C.MAX_CONTENT_LENGTH)

    def test_question_answering(self):
        phrase = 'What is microkernel architecture?'
        corpus = [page['text'] for page in self.extracts]

        answer = AnswerService.generate_answer(phrase, corpus, AnswerModel.SPAN_BERT_SQUAD)

        self.assertIsNotNone(answer)
        self.assertGreater(len(answer), C.MIN_ANSWER_LENGTH)
        self.assertLess(len(answer), C.MAX_ANSWER_LENGTH)

    @skipIf(True, 'Memory intensive')
    def test_abstractive_summarization(self):
        phrase = 'What is microkernel architecture?'
        corpus = [page['text'] for page in self.extracts]

        summary = SummaryService.generate_summary(phrase, corpus, SummaryModel.DISTILL_BART_CNN)

        self.assertIsNotNone(summary)
        self.assertGreater(len(summary.split(' ')), C.MIN_SUMMARY_LENGTH)
        self.assertLess(len(summary.split(' ')), C.MAX_SUMMARY_LENGTH)
