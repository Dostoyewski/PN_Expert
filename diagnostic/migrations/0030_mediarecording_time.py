# Generated by Django 3.1.5 on 2021-12-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0029_auto_20211102_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediarecording',
            name='time',
            field=models.FloatField(default=0),
        ),
    ]