# Generated by Django 3.1.5 on 2021-10-04 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnostic', '0024_doctorevent_mediarecording'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorevent',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doctorevent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]