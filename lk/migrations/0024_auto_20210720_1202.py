# Generated by Django 3.1.5 on 2021-07-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lk', '0023_userprofile_reminders'),
    ]

    operations = [
        migrations.AddField(
            model_name='hads_alarm',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hads_result',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
