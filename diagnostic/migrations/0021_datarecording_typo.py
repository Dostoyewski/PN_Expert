# Generated by Django 3.1.5 on 2021-07-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0020_pushnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarecording',
            name='typo',
            field=models.IntegerField(
                choices=[(0, 'Обследование'), (1, 'Операция'), (2, 'Тест'), (3, 'Препараты'), (4, 'Анализы'),
                         (5, 'Другое')], default=5),
        ),
    ]
