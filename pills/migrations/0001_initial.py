# Generated by Django 3.1.5 on 2021-04-26 13:17

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('info', models.TextField(max_length=1000)),
                ('dosege', models.CharField(max_length=500)),
                ('end', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField(default=datetime.time(16, 0))),
                ('extra', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='AssignedPill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pills.pill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
