# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-03 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
