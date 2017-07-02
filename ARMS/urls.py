"""ARMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from timer.views import TimerView
from register.views import RegisterView, RegistResultView, SearcherView, HomeView
from waiter.views import ArrangementView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^searcher/', SearcherView.as_view(), name='searcher'),
    url(r'^waiter/', ArrangementView.as_view(), name='waiter'),
    url(r'^regist_result/', RegistResultView.as_view(), name='result'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^timer/', TimerView.as_view(), name='timer'),
    url(r'^admin/', admin.site.urls),
]
