# Generated by Django 3.1.5 on 2021-07-19 18:31

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pills', '0009_pillsreseter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillsreseter',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
