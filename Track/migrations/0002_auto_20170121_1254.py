# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='track_genre',
            field=models.CharField(max_length=30),
        ),
    ]