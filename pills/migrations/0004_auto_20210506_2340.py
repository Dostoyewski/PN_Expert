# Generated by Django 3.1.5 on 2021-05-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pills', '0003_auto_20210506_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pill',
            name='is_taken',
        ),
        migrations.RemoveField(
            model_name='pill',
            name='time_out',
        ),
        migrations.AddField(
            model_name='assignedpill',
            name='is_taken',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='assignedpill',
            name='time_out',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]