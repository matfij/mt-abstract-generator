from django.utils import timezone
from django.db.models import Model, CharField, TextField, FloatField, BooleanField, IntegerField, DateTimeField
from django_mysql.models import ListCharField

from generator.constants import AnswerModel, SummaryModel


class GenerateAbstractParams:
    PAGE_NUMBER_DEFAULT = 20
    ANSWER_MODEL_DEFAULT = AnswerModel.ELECTRA_SQUAD.value
    SUMMARY_MODEL_DEFAULT = SummaryModel.DISTILL_BART_CNN.value

    def __init__(self, data: dict):
        self.phrase = data.get('phrase')
        self.page_number = data.get('page_number', self.PAGE_NUMBER_DEFAULT)
        self.answer_model = data.get('answer_model', self.ANSWER_MODEL_DEFAULT)
        self.summary_model = data.get('summary_model', self.SUMMARY_MODEL_DEFAULT)


class ResultPageModel(Model):
    url = CharField(max_length=255)
    references = ListCharField(
        base_field=CharField(max_length=255),
        size=50,
        max_length=255*51
    )
    content = TextField(blank=True, default=None, null=True)
    quality = FloatField(blank=True, default=None, null=True)


class AbstractModel(Model):
    answer = TextField(max_length=511)
    summary = TextField(max_length=4095)


class KeyModel(Model):
    key = CharField(max_length=255)
    tester_name = CharField(max_length=255, null=True)
    tester_class = IntegerField(default=1, null=True)
    active = BooleanField(default=True)
    creation_date = DateTimeField(default=timezone.now)
    use_count = IntegerField(default=0)
    use_limit = IntegerField(default=10)
