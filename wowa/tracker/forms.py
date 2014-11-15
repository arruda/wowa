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
    Form for the creation of a Character for a user
    """

    class Meta:
        model = Character
        fields = ('name', 'realm',)

    def save(self):
        character = super(CharacterForm, self).save(commit=False)
        character.user = self.user
        character.save()
        return character
