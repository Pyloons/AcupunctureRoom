# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Arrangement(models.Model):
    number = models.IntegerField(verbose_name=u'排号')
    name = models.CharField(verbose_name=u'姓名', max_length=10)
    has_treated = models.BooleanField(verbose_name=u'是否已确定治疗', default=False)
    skip = models.BooleanField(verbose_name=u'暂时跳过', default=False)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = u'安排表'
        verbose_name_plural = verbose_name
