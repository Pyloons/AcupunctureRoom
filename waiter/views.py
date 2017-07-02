# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import Arrangement
from register.models import Register


class ArrangementView(View):
    def get(self, request):
        # 最大排号
        max_num = Arrangement.objects.order_by('-number')
        if len(max_num) > 0:
            max_num = max_num[0]
        else:
            max_num = '无人排队'

        # 最大已治疗排号
        max_treated_num = Arrangement.objects.filter(has_treated=True).order_by('-number')
        if len(max_treated_num) > 0:
            max_treated_num = max_treated_num[0]
        else:
            max_treated_num = 0

        # 下一个排号
        # 该处有误，由于序号清奇，简单+1并不能得到下一个序号，不应当使用
        # next_num = max_treated_num.number + 1

        # 未治疗且未跳过患者
        untreated_patient_normal = Arrangement.objects.filter(has_treated=False, skip=False).order_by('number')

        # 未治疗且已跳过患者
        untreated_patient_skiped = Arrangement.objects.filter(has_treated=False, skip=True).order_by('number')

        return render(request, 'waiter.html', {'maxNum': max_num,
                                               'maxTreat': max_treated_num,
                                               'unTreat': untreated_patient_normal,
                                               'skiped': untreated_patient_skiped})

    def post(self, request):
        data = request.POST
        if data['type'] == 'arrangement':
            new_arrangement = Arrangement(number = data['number'], name = data['name'])
            new_arrangement.save()
        elif data['type'] == 'treat':
            new_arrangement = Arrangement.objects.get(number=data['number'])
            new_arrangement.has_treated = True
            new_arrangement.save()
            new_treat_log = Register(name=data['name'],type='zl')
            new_treat_log.save()
        elif data['type'] == 'skip':
            new_arrangement = Arrangement.objects.get(number=data['number'])
            new_arrangement.skip = True
            new_arrangement.save()
        return HttpResponseRedirect('/waiter/')

