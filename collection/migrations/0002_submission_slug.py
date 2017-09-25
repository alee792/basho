# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
