# Generated by Django 3.1.7 on 2021-05-03 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210503_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 18, 48, 5, 157946)),
        ),
    ]
