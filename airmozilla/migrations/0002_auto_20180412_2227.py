# Generated by Django 1.11.12 on 2018-04-12 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airmozilla', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_key',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
