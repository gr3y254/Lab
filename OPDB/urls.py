'''
Created on Aug 30, 2016

@author: Manu
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]