# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airmozilla', '0007_auto_20180418_1640'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TRIGGER update_event_fulltext BEFORE INSERT OR UPDATE
                ON airmozilla_event FOR EACH ROW EXECUTE PROCEDURE
                update_event_fulltext();
            """,
            """
            DROP TRIGGER update_event_fulltext ON airmozilla_event;
            """
        ),
    ]
