# Generated by Django 3.1.5 on 2021-04-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0008_auto_20210401_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='survey_pk',
            field=models.IntegerField(default=0),
        ),
    ]
