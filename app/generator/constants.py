from enum import Enum


class AnswerModel(Enum):
    SPAN_BERT_SQUAD = 1
    ELECTRA_SQUAD = 2
    GPT2 = 3


class SummaryModel(Enum):
    DISTILL_BART_CNN = 1
    DISTILL_PEGASUS_CNN = 2
