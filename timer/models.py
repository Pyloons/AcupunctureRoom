# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Timer(models.Model):
    bed_num = models.IntegerField(verbose_name=u'床位号')
    start_time = models.CharField(verbose_name=u'开始时间', blank=True, null=True, max_length=100)
    end_time = models.CharField(verbose_name=u'结束时间', blank=True, null=True, max_length=100)
    more_end_time = models.IntegerField(verbose_name=u'结束加时', blank=True, null=True)
    middle_time = models.CharField(verbose_name=u'中间时间', blank=True, null=True, max_length=100)
    more_middle_time = models.IntegerField(verbose_name=u'中间加时', blank=True, null=True)

    def __str__(self):
        return str(self.bed_num)

    class Meta:
        verbose_name = u'计时器'
        verbose_name_plural = verbose_name
