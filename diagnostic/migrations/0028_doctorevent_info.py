# Generated by Django 3.1.5 on 2021-11-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0027_auto_20211004_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorevent',
            name='info',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
