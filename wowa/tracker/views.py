# -*- coding: utf-8 -*-
"""
    tracker.views
    ~~~~~~~~~~~~~~

    tracker views file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

# view imports
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView


from .models import Character, Item
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
    model = Item
    template_name = 'tracker/tracked_items_list.html'

    def get_queryset(self):
        chars = self.request.user.characters.all()

        items_ids = []

        for c in chars:
            ids = c.items.all().values_list('pk', flat=True)
            items_ids.extend(ids)
        queryset = super(TrackedItemsListView, self).get_queryset()
        return queryset.filter(pk__in=items_ids)
