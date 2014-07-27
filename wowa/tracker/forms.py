#-*- coding:utf-8 -*-
"""
    tracker.forms
    ~~~~~~~~~~~~~~

    tracker forms file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

from django import forms

from .models import Character

class CharacterForm(forms.ModelForm):
    """
    Form para criação de um novo character de um determinado realm para um usuario
    """

    class Meta:
        model = Character
        fields = ('name', 'realm',)
