# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20171008_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
