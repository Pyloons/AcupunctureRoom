# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0002_auto_20170630_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='timer',
            name='middle_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u4e2d\u95f4\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='timer',
            name='more_middle_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u4e2d\u95f4\u52a0\u65f6'),
        ),
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]
