# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def characterNameToCharacterRealmConnection(apps, schema_editor):
    "create a connection for all character to their realms based on the realm_name field"

    Realm = apps.get_model("tracker", "Realm")
    Character = apps.get_model("tracker", "Character")
    for char in Character.objects.all():
        realm_name = char.realm_name
        realm = Realm.objects.get(name=realm_name)
        char.realm = realm
        char.save()


def revert(apps, schema_editor):
    "revert back deleting the connection on Charactger x Realm"

    Character = apps.get_model("tracker", "Character")
    for char in Character.objects.all():
        char.realm = None
        char.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_character_realm'),
    ]

    operations = [
        migrations.RunPython(characterNameToCharacterRealmConnection, reverse_code=revert),
    ]
