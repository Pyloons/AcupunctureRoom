# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Timer


class TimerAdmin(admin.ModelAdmin):
    list_display = ('bed_num', 'start_time', 'end_time', 'more_end_time', 'middle_time', 'more_middle_time')

admin.site.register(Timer, TimerAdmin)
