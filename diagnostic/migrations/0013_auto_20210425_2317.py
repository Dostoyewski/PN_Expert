# Generated by Django 3.1.5 on 2021-04-25 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('survey', '0004_auto_20210407_1303'),
        ('diagnostic', '0012_auto_20210425_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startevent',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey'),
        ),
    ]