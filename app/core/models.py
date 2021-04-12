from django.db.models import Model, CharField, TextField, FloatField
from django_mysql.models import ListCharField


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
