# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from register.models import Register


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        data = request.POST
        new_log = Register(name=data['name'], times=data['times'], type=data['type'])
        new_log.save()
        # pdb.set_trace()
        return HttpResponseRedirect('/regist_result/')


class RegistResultView(View):
    def get(self, request):
        data = Register.objects.order_by('-date')[0]
        return render(request, 'regist_result.html', {'result': data})


class SearcherView(View):
    def get(self, request):
        return render(request, 'searcher.html')

    def post(self, request):
        data = request.POST
        result = Register.objects.filter(name = data['name']).order_by('-date')
        return render(request, 'search_result.html', {'result': result})

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage.html')
