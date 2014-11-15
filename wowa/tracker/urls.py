# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from tracker import views

urlpatterns = patterns('tracker.views',
    url(r'^new_char/$', views.CharacterCreateView.as_view(), name='new_char'),
    url(r'^chars/$', views.CharacterListView.as_view(), name='my_chars'),
    url(r'^del_char/(?P<pk>\d+)/$', views.CharacterDeleteView.as_view(), name='rm_char'),
    url(r'^tracked/$', 'tracked_items', name='tracked_items'),
)
