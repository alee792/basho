# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_submission_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='slug',
        ),
    ]
