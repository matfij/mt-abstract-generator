import datetime

from django.db.models import Model, CharField, TextField, FloatField, IntegerField, DateTimeField
from django_mysql.models import ListCharField


class PollModel(Model):
    key = CharField(max_length=255)
    subject_name = CharField(max_length=255)
    date = DateTimeField(default=datetime.datetime.now())
    phrase = CharField(max_length=255)
    answer_model = IntegerField()
    summary_model = IntegerField()
    answer_score = FloatField()
    summary_score = FloatField()
    answer = TextField(blank=True, default=None, null=True)
    summary = TextField(blank=True, default=None, null=True)
