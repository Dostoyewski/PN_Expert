# Generated by Django 3.1.5 on 2021-06-01 14:25

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lk', '0011_userprofile_issick'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepsCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now)),
                ('steps', models.IntegerField(default=-1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]