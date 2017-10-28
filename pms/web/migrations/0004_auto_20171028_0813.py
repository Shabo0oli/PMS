# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_bar_bartime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DueDate', django_jalali.db.models.jDateField()),
                ('StudyHour', models.IntegerField(blank=True)),
                ('TestNumber', models.IntegerField(blank=True)),
                ('CourseName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Course')),
                ('StudentName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='Bar',
        ),
        migrations.DeleteModel(
            name='BarTime',
        ),
    ]
