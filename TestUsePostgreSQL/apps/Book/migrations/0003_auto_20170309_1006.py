# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_book_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Book'},
        ),
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
