# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='auto_increment_id',
        ),
        migrations.AddField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
