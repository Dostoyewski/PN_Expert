# Generated by Django 3.1.5 on 2021-07-12 20:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('lk', '0021_hads_alarm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hads_alarm',
            old_name='depression',
            new_name='alarm',
        ),
    ]
