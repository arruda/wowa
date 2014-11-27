# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import models, migrations


def itemCharacterToCharacterItemModel(apps, schema_editor):
    "copy the data of all M2M (Item x Character) in the CharacterItem Model"

    Item = apps.get_model("tracker", "Item")
    CharacterItem = apps.get_model("tracker", "CharacterItem")
    for item in Item.objects.all():
        for character in item.characters.all():
            character_item = CharacterItem(item=item, character=character)
            character_item.save()


def revert(apps, schema_editor):
    "revert back deleting the CharacterItem for each Item"

    Item = apps.get_model("tracker", "Item")
    CharacterItem = apps.get_model("tracker", "CharacterItem")
    for item in Item.objects.all():
        for character in item.characters.all():
            try:
                character_item = CharacterItem.objects.get(item=item, character=character)
                character_item.delete()
            except ObjectDoesNotExist:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_item_characters_new'),
    ]

    operations = [
        migrations.RunPython(itemCharacterToCharacterItemModel, reverse_code=revert),
    ]
