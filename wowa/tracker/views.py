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
