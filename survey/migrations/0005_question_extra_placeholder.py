# Generated by Django 3.2.4 on 2021-06-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('survey', '0004_auto_20210407_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='extra_placeholder',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
