# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-22 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userModule', '0011_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='isDetailsProvided',
            field=models.CharField(default='no', max_length=10),
        ),
    ]