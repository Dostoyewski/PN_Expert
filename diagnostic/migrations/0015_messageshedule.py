# Generated by Django 3.1.5 on 2021-05-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0014_startshedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageShedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_interval', models.IntegerField(
                    choices=[(0, 'Ежедневно'), (1, 'Раз в неделю'), (2, 'Раз в месяц'), (3, 'Раз в квартал')],
                    default=0)),
                ('message', models.TextField(default=' ')),
                ('typo', models.IntegerField(
                    choices=[(0, 'Мероприятие'), (1, 'Прием лекарств'), (2, 'Видео тест'), (3, 'Отправка фотографии'),
                             (4, 'Опрос')])),
                ('forall', models.BooleanField(default=False)),
                ('location', models.CharField(default=' ', max_length=1000)),
            ],
        ),
    ]
