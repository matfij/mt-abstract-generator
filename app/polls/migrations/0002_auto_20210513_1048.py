# Generated by Django 3.1.7 on 2021-05-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollmodel',
            name='answer_score',
        ),
        migrations.RemoveField(
            model_name='pollmodel',
            name='summary_score',
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='answer_score_grammatical',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='answer_score_logical',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='summary_score_grammatical',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pollmodel',
            name='summary_score_logical',
            field=models.FloatField(default=0),
        ),
    ]
