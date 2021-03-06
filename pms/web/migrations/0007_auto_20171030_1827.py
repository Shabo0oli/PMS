# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20171028_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='done',
            name='CourseName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Course'),
        ),
        migrations.AlterField(
            model_name='done',
            name='StudentName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Student'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='StudentName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Student'),
        ),
    ]
