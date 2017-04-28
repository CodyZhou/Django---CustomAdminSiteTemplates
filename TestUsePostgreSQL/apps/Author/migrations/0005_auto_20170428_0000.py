# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 00:00
from __future__ import unicode_literals

import TestUsePostgreSQL.apps.validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0004_auto_20170315_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(help_text='Please input all digital. For Example: 6261234567.', max_length=20, validators=[TestUsePostgreSQL.apps.validation.validator_number]),
        ),
    ]
