# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Arrangement


class ArrangementAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'has_treated', 'skip')

admin.site.register(Arrangement, ArrangementAdmin)
