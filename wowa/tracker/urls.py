# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from tracker import views

urlpatterns = patterns('tracker.views',
    url(regex=r'^new_char/$',
        view=views.CharacterCreateView.as_view(),
        name='new_char'),
    url(regex=r'^chars/$',
        view=views.CharacterListView.as_view(),
        name='my_chars'),
    url(regex=r'^del_char/(?P<pk>\d+)/$',
        view=views.CharacterDeleteView.as_view(),
        name='rm_char'),
    url(regex=r'^my_items/$',
        view=views.TrackedItemsListView.as_view(),
        name='tracked_items_list'),
    url(
        regex=r'^my_items/(?P<pk>\d+)/$',
        view=views.TrackItemDetailView.as_view(),
        name='tracked_item'
    ),
)
