# Generated by Django 3.1.5 on 2021-07-19 18:28

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pills', '0008_alter_assignedpill_time_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='PillsReseter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=datetime.time(0, 0))),
            ],
        ),
    ]
