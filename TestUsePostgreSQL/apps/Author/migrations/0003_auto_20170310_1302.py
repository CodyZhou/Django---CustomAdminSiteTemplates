# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-10 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0002_auto_20170309_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoraddress',
            name='address_2',
            field=models.CharField(blank=True, help_text='Apt. No., Suite No. and so on.<br>This length is no more than 50 characters.', max_length=50),
        ),
    ]