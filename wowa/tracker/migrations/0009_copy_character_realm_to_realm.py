# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations


def characterReamToRealModel(apps, schema_editor):
    "copy the data of Character.realm to a Realm model"

    Realm = apps.get_model("tracker", "Realm")
    Character = apps.get_model("tracker", "Character")
    for char in Character.objects.all():
        realm_name = char.realm
        # incase it exist don't do anything
        try:
            Realm.objects.get(name=realm_name)
        except ObjectDoesNotExist:
            # it doesn't exist, should create one
            realm = Realm(name=realm_name)
            realm.save()


def revert(apps, schema_editor):
    "revert back deleting the Realm"

    Realm = apps.get_model("tracker", "Realm")
    Realm.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_realm'),
    ]

    operations = [
        migrations.RunPython(characterReamToRealModel, reverse_code=revert),
    ]
