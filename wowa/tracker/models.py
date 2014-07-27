# -*- coding: utf-8 -*-
"""
    tracker.models
    ~~~~~~~~~~~~~~

    tracker models file

    :copyright: (c) 2014 by arruda.
"""

from django.db import models


class Item(models.Model):
    """
    Represents a Item that is tracked
    """

    b_id = models.PositiveIntegerField(u"Blizzard Item Id", blank=False, null=True)
    name = models.CharField(u"Item Name", max_length=350, blank=True, null=True)

    class Meta:
        app_label = 'tracker'

    def __unicode__(self):

        if self.name is None:
            return self.name
        else:
            return "#" + str(self.b_id)
