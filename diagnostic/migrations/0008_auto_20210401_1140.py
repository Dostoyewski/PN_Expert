# Generated by Django 3.1.5 on 2021-04-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0007_auto_20210401_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarecording',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]