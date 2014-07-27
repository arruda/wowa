# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('tracker.views',
    url(r'^new_char/$', 'new_char', name='new_char'),
    url(r'^chars/$', 'my_chars', name='my_chars'),
)
