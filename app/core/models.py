from django.db.models import CharField, Model
from django_mysql.models import ListCharField


class AbstractModel(Model):
    urls = ListCharField(
        base_field=CharField(max_length=255),
        size=50,
        max_length=255*51
    )
