from django.utils import timezone
from django.db.models import Model, CharField, TextField, FloatField, IntegerField, DateTimeField
from django_mysql.models import ListCharField

from generator.constants import AnswerModel, SummaryModel


class PollModel(Model):
    key = CharField(max_length=255, null=True)
    date = DateTimeField(default=timezone.now)
    phrase = CharField(max_length=255)
    answer_model = IntegerField()
    summary_model = IntegerField()
    page_number = IntegerField()
    answer_score_logical = FloatField(default=0)
    answer_score_grammatical = FloatField(default=0)
    summary_score_logical = FloatField(default=0)
    summary_score_grammatical = FloatField(default=0)
    time_score = FloatField()
    answer = TextField(blank=True, default=None, null=True)
    summary = TextField(blank=True, default=None, null=True)
    comment = TextField(blank=True, default=None, null=True)
