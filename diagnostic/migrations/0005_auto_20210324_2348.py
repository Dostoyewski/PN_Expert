# Generated by Django 3.1.5 on 2021-03-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0004_dailyactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
