# Generated by Django 3.1.5 on 2021-04-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0009_event_survey_pk'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
