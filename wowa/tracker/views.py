# -*- coding: utf-8 -*-
"""
    tracker.views
    ~~~~~~~~~~~~~~

    tracker views file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

# view imports
import json

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView
# from django.views.generic import RedirectView
# from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView


from .models import Character, Item, CharacterItem
from .forms import CharacterForm

from .utils import JSONLazyEncoder


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

    def get_chart_data(self):
        "return the chart's data that will be used with Chart.js"
        data = {}
        data['labels'] = self.get_chart_labels()
        data['datasets'] = self.get_chart_datasets()

        return data

    def get_chart_labels(self):
        "return the chart's labels"
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_chart_datasets(self):
        "the datasets used in the chart"
        datasets = []
        global_item_price_dataset = self.get_chart_char_item_price_dataset()
        char_item_price_dataset = self.get_chart_global_item_price_dataset()
        datasets.append(global_item_price_dataset)
        datasets.append(char_item_price_dataset)
        return datasets

    def get_chart_char_item_price_dataset(self):
        "the dataset for the character's item price"
        dataset = {
            'label': _('My Price'),
            'fillColor': "rgba(151,187,205,0.2)",
            'strokeColor': "rgba(151,187,205,1)",
            'pointColor': "rgba(151,187,205,1)",
            'pointStrokeColor': "#fff",
            'pointHighlightFill': "#fff",
            'pointHighlightStroke': "rgba(151,187,205,1)",
        }
        dataset['data'] = self.get_chart_char_item_price_dataset_data()
        return dataset

    def get_chart_char_item_price_dataset_data(self):
        "Dataset's data for the character's item price"
        return [28, 48, 40, 19, 86, 27, 90]

    def get_chart_global_item_price_dataset(self):
        "the dataset for the global item price"
        dataset = {
            'label': _('Global Minimum Price'),
            'fillColor': "rgba(220,220,220,0.2)",
            'strokeColor': "rgba(220,220,220,1)",
            'pointColor': "rgba(220,220,220,1)",
            'pointStrokeColor': "#fff",
            'pointHighlightFill': "#fff",
            'pointHighlightStroke': "rgba(220,220,220,1)",
        }
        dataset['data'] = self.get_chart_global_item_price_dataset_data()
        return dataset

    def get_chart_global_item_price_dataset_data(self):
        "Dataset's data for the global item price"
        return [65, 59, 80, 81, 56, 55, 40]

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            data_json = json.dumps(self.get_chart_data(), cls=JSONLazyEncoder, indent=1)
            context['chart_data'] = data_json

        return super(TrackItemDetailView, self).get_context_data(**context)
