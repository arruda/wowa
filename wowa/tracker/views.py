# -*- coding: utf-8 -*-
"""
    tracker.views
    ~~~~~~~~~~~~~~

    tracker views file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

# view imports
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView
# from django.views.generic import RedirectView
# from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView


from .models import Character, Item, CharacterItem
from .forms import CharacterForm


class CharacterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Character
    form_class = CharacterForm
    success_url = reverse_lazy("tracker:my_chars")
    success_message = "New character %(name)s/%(realm)s was created."

    def form_valid(self, form):
        """
        If the form is valid, add the current user as the character user.
        then proceed to saving the form.
        """
        form.user = self.request.user
        return super(CharacterCreateView, self).form_valid(form)


class CharacterListView(LoginRequiredMixin, ListView):
    model = Character

    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class CharacterDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Character
    success_url = reverse_lazy("tracker:my_chars")

    def get_object(self, queryset=None):
        """ Hook to ensure character is owned by request.user. """
        obj = super(CharacterDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class TrackedItemsListView(LoginRequiredMixin, ListView):
    model = CharacterItem
    template_name = 'tracker/tracked_character_items_list.html'

    def get_queryset(self):
        user_chars = self.request.user.characters.all()

        queryset = super(TrackedItemsListView, self).get_queryset()
        return queryset.filter(character__in=user_chars)


class TrackItemDetailView(LoginRequiredMixin, DetailView):
    model = CharacterItem
    template_name = 'tracker/character_item_detail.html'


    # slug_field = "username"
    # slug_url_kwarg = "username"
