# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='image',
            name='embed_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='low_res_url',
            field=models.URLField(),
        ),
    ]
