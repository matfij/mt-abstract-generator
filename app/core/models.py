from django.db.models import CharField, Model
from django_mysql.models import ListCharField


class ResultPageModel(Model):
    url = CharField(max_length=255)
    references = ListCharField(
        base_field=CharField(max_length=255),
        size=50,
        max_length=255*51
    )
