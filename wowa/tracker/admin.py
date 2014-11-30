#-*- coding:utf-8 -*-
"""
    tracker.admin
    ~~~~~~~~~~~~~~

    tracker admin file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

from django.contrib import admin

from .models import Realm
from .models import Item
from .models import Character
from .models import CharacterItem
from .models import RealmItemPriceOnDate
from .models import CharacterItemPriceOnDate


admin.site.register(Realm, admin.ModelAdmin)

admin.site.register(Character, admin.ModelAdmin)

admin.site.register(Item, admin.ModelAdmin)
admin.site.register(CharacterItem, admin.ModelAdmin)
admin.site.register(RealmItemPriceOnDate, admin.ModelAdmin)
admin.site.register(CharacterItemPriceOnDate, admin.ModelAdmin)
