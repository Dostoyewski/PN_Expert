# Generated by Django 3.1.5 on 2021-09-15 23:45

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lk', '0034_pdq39stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyActivityStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now)),
                ('sleep_time', models.FloatField(default=0)),
                ('no_hom_time', models.FloatField(default=0)),
                ('work_time', models.FloatField(default=0)),
                ('sport_time', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
