# -*- coding: utf-8 -*-
"""
    tracker.models
    ~~~~~~~~~~~~~~

    tracker models file

    :copyright: (c) 2014 by arruda.
"""

from django.db import models


class Realm(models.Model):
    """
    A Wow realm
    """
    name = models.CharField(u"Realm Name", max_length=350, blank=False, null=True)

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):
        return self.name


class Character(models.Model):
    """
    A wow character
    """

    name = models.CharField(u"Character Name", max_length=350, blank=False, null=True)
    realm = models.ForeignKey('tracker.Realm', related_name=u"characters", blank=False, null=True)

    user = models.ForeignKey('users.User', related_name=u"characters", blank=True, null=True)

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):

        return "%s / %s" % (self.realm, self.name)


class CharacterItem(models.Model):
    """
    The connection of Character and Item
    """

    item = models.ForeignKey('tracker.Item', related_name='character_items')
    character = models.ForeignKey('tracker.Character', related_name='character_items')

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):
        return "%s - %s" % (self.item, self.character)


class Item(models.Model):
    """
    Represents an Item that is tracked
    """

    blizzard_id = models.PositiveIntegerField(u"Blizzard Item Id", blank=False, null=True)
    name = models.CharField(u"Item Name", max_length=350, blank=True, null=True)

    characters = models.ManyToManyField(
        Character,
        through=CharacterItem,
        related_name=u"items",
        blank=True, null=True
    )

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):

        if self.name is None:
            return "#" + str(self.b_id)
        else:
            return self.name + " (" + "#" + str(self.blizzard_id) + ")"


class RealmItemPriceOnDate(models.Model):
    """
    Represent the informations of price for a given Item
    in a Realm, on given a Date
    """

    realm = models.ForeignKey(
        'tracker.Realm',
        related_name=u"item_prices_on_date",
        blank=False, null=True
    )

    item = models.ForeignKey(
        'tracker.Item',
        related_name=u"item_prices_on_date",
        blank=False, null=True
    )

    date = models.DateField(u"Date", auto_now_add=True, blank=False, null=True)

    def __unicode__(self):
        return "%s %s %s" % (self.realm, self.item, self.date)
