# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170205_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog/media'),
            preserve_default=False,
        ),
    ]
