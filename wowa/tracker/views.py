# -*- coding: utf-8 -*-
"""
    tracker.views
    ~~~~~~~~~~~~~~

    tracker views file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

# view imports
from django.db.models import Q
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView


# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect

from allauth.account.adapter import get_adapter

from .models import Character, Item
from .forms import CharacterForm


class CharacterCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Character
    form_class = CharacterForm
    success_url = reverse_lazy("tracker:my_chars")
    success_message = "New character %(name)s/%(realm)s was created."


class CharacterListView(LoginRequiredMixin, ListView):
    model = Character

    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


@login_required
# @render_to('tracker/my_chars.html')
def my_chars(request):
    "list all characters for a user"
    characters = request.user.characters.all()
    return {'characters': characters}


# @login_required
# # @render_to('tracker/new_char.html')
# def new_char(request):
#     "create a character for the logged user"

#     user = request.user

#     if request.method == "POST":
#         form = CharacterForm(request.POST)
#         if form.is_valid():
#             new_char = form.save(commit=False)
#             new_char.user = user
#             new_char.save()
#             get_adapter().add_message(request,
#                                       messages.SUCCESS,
#                                       'tracker/messages/char_created.txt',
#                                       {'character': new_char})

#             return redirect('tracker:my_chars')
#     else:
#         form = CharacterForm()
#     return locals()


@login_required
# @render_to('tracker/my_chars.html')
def rm_char(request, char_id):
    "rm a character for the logged user"
    character = get_object_or_404(Character, pk=char_id)

    if request.method == "POST":

        if character.user.pk is request.user.pk:
            character.delete()
            get_adapter().add_message(request,
                                      messages.SUCCESS,
                                      'tracker/messages/char_removed.txt',
                                      {'character': character})

    return redirect('tracker:my_chars')


@login_required
# @render_to('tracker/tracked_items.html')
def tracked_items(request):
    "list all tracked items for this user"

    chars = request.user.characters.all()

    #import pdb;pdb.set_trace()
    items_ids = []

    for c in chars:
        ids = c.items.all().values_list('pk', flat=True)
        items_ids.extend(ids)

    items = Item.objects.filter(pk__in=items_ids)

    return {'items': items}
