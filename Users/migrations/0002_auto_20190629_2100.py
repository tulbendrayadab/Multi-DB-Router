# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-29 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
