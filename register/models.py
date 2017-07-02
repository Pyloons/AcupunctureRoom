# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as tz


class Register(models.Model):
    date = models.DateTimeField(verbose_name=u'登记日期', default=tz.now)
    name = models.CharField(verbose_name=u'姓名', max_length=10)
    times = models.IntegerField(verbose_name=u'登记次数', blank=True, null=True)
    type = models.CharField(verbose_name=u'记录类型', max_length=2, choices=(('dj', u'登记'), ('zl', u'治疗')))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = u'注册记录'
        verbose_name_plural = verbose_name

