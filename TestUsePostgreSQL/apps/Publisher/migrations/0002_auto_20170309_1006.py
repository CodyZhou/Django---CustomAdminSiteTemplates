# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publisher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Publisher', 'verbose_name_plural': 'Publisher'},
        ),
        migrations.AlterField(
            model_name='publisher',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
