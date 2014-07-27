# -*- coding: utf-8 -*-
"""
    tracker.models
    ~~~~~~~~~~~~~~

    tracker models file

    :copyright: (c) 2014 by arruda.
"""

from django.db import models


class Character(models.Model):
    """
    An wow character
    """

    name = models.CharField(u"Character Name", max_length=350, blank=False, null=True)
    realm = models.CharField(u"Realm", max_length=350, blank=False, null=True)

    user = models.ForeignKey('auth.User', related_name=u"characters", blank=True, null=True)

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):

        return self.realm + "/" + self.name


class Item(models.Model):
    """
    Represents a Item that is tracked
    """

    b_id = models.PositiveIntegerField(u"Blizzard Item Id", blank=False, null=True)
    name = models.CharField(u"Item Name", max_length=350, blank=True, null=True)

    characters = models.ManyToManyField(Character, related_name=u"Items", blank=True, null=True)

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):

        if self.name is None:
            return self.name
        else:
            return "#" + str(self.b_id)
