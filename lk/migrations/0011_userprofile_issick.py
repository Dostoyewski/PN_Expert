# Generated by Django 3.1.5 on 2021-05-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lk', '0010_auto_20210516_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isSick',
            field=models.BooleanField(default=False),
        ),
    ]