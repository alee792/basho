# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_remove_submission_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='elo',
            field=models.IntegerField(default=1000),
        ),
    ]