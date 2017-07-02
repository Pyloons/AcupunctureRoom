# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import pdb

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import Timer


class TimerView(View):
    def get(self, request):
        timer = Timer.objects.all()
        # pdb.set_trace()
        return render(request, 'time_limit.html', {'all': timer})

    def post(self, request):
        data = request.POST
        the_bed = Timer.objects.get(bed_num=data['form_bed'])

        the_bed.start_time = data['form_start']

        the_bed.end_time = data['form_end']

        if data['form_add2'] == '':
            the_bed.more_end_time = 0
        else:
            the_bed.more_end_time = data['form_add1']

        the_bed.middle_time = data['form_mid']

        if data['form_add2'] == '':
            the_bed.more_middle_time = 0
        else:
            the_bed.more_middle_time = data['form_add2']

        the_bed.save()

        # pdb.set_trace()
        return HttpResponseRedirect('/timer/')
