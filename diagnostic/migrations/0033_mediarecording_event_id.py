# Generated by Django 3.2.4 on 2021-12-13 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0032_auto_20211205_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediarecording',
            name='event_id',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='diagnostic.event'),
        ),
    ]