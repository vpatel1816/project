# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.article_list),
]
