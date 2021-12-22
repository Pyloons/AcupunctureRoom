"""ARMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from timer.views import TimerView
from register.views import RegisterView, RegistResultView, SearcherView, HomeView
from waiter.views import ArrangementView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('searcher/', SearcherView.as_view(), name='searcher'),
    path('waiter/', ArrangementView.as_view(), name='waiter'),
    path('regist_result/', RegistResultView.as_view(), name='result'),
    path('register/', RegisterView.as_view(), name='register'),
    path('timer/', TimerView.as_view(), name='timer'),
    path('admin/', admin.site.urls),
]

'''
urlpatterns = [
    path(r'^$', HomeView.as_view(), name='home'),
    path(r'^searcher/', SearcherView.as_view(), name='searcher'),
    path(r'^waiter/', ArrangementView.as_view(), name='waiter'),
    path(r'^regist_result/', RegistResultView.as_view(), name='result'),
    path(r'^register/', RegisterView.as_view(), name='register'),
    path(r'^timer/', TimerView.as_view(), name='timer'),
    path(r'^admin/', admin.site.urls),
]
'''
