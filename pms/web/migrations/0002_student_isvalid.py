# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='IsValid',
            field=models.BooleanField(default=False),
        ),
    ]
